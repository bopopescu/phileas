#!/usr/bin/python

import argparse, sys, os, subprocess, pickle, re
sys.path.append('../lib')
import time, pprint
import yaml
from big_query.bigquery_object import BigQueryObject
from big_query.bigquery_schema import BigQueryMaker
from threading import Thread

args = None
pkb_cmd = os.pardir + '/lib/PerfKitBenchmarker/pkb.py'

def main():
    assert args.cloud is not None
    assert args.tests is not None
    assert args.config_file is not None and os.path.exists(args.config_file)
    test_file = open(args.config_file)
    data_dict = yaml.load(test_file)
    assert data_dict['test_suite'] is not None and data_dict['results_location'] is not None
    test_suite = data_dict['test_suite']
    for cloud_provider in test_suite:
        if cloud_provider['cloud'] in args.cloud:
            t = Thread(target=execute, args=([cloud_provider, data_dict['results_location'], data_dict['project_id'], data_dict['dataset']]))
            t.start()

def execute(cloud_provider, results_location, project_id, dataset):
    results_location += cloud_provider['cloud']
    pkb_run = create_run_cmd(cloud_provider, results_location)
    assert pkb_run is not None
    create_results_dir(cloud_provider, results_location)
    results_pkb = None
    if args.dryrun is not True:
        results_pkb = run(pkb_run)
        if (results_pkb != 1):
            print results_pkb
            sys.exit(1)
    tests = list(args.tests)
    schema_cmd = extract_schema(results_location, cloud_provider['cloud'], tests)
    if (schema_cmd is not True):
        raise Exception("Schema could not be extracted. Exiting...")
    else:
        for test in args.tests:
            success = export_results(cloud_provider['cloud'], results_location, test, project_id, dataset)
            if (success is not True):
                raise Exception("Something went wrong with loading the data into the cloud. Exiting...\nERROR:" + str(success))




def export_results(cloud_provider, results_location, test, project_id, dataset):
    results_file = results_location + '/results.json'
    bq = BigQueryObject(project_id)
    if bq.check_dataset(dataset) is not True:
        result = bq.create_dataset(dataset, "Dataset for analyzing cloud performance")
        assert result is True
    if bq.check_table(dataset, test) is not True:
        schema_loc = '../lib/providers/' + cloud_provider + '/schema/' + 'table_' + test + '.json'
        result = bq.create_table(dataset, test, schema_loc)
        assert result is True
    result = bq.add_data_to_table(dataset, test, results_file)
    return result

def extract_schema(results_location, cloud, tests):
    results_file = results_location + '/results.json'
    schema_maker = BigQueryMaker()
    try:
        schema_maker.create_schema(results_file, cloud, tests)
    except Exception as e:
        print str(e)
        return False
    return True

def run(command):
    try:
        subprocess.check_output(command)
    except subprocess.CalledProcessError as e:
        print str(e)
        if e.output.startswith('error: {'):
            error = json.loads(e.output[7:])
            return [ error['code'], error['message'] ]
        else:
            return e.output
    return 1


def create_results_dir(cloud_provider, results_location):
    if not os.path.isdir(results_location):
        os.umask(0)
        os.makedirs(results_location)
        os.chown(results_location, os.getuid(), -1)
    else:
        return

def create_run_cmd(cloud_provider, results_location):
    pkb_run = [pkb_cmd]
    pkb_run.extend(["--cloud", cloud_provider['cloud']])
    if 'globals' in cloud_provider.keys():
        for option, value in cloud_provider['globals'].iteritems():
            pkb_run.extend(["--" + option, str(value)])
    pkb_run.extend(["--ignore_package_requirements", "--nocollapse_labels"])
    tests_to_run = []
    for test in cloud_provider['tests']:
        if test['test'] in args.tests or 'all' in args.tests:
            tests_to_run.append(test['test'])
            if 'options' in test.keys():
                for option in test['options']:
                    pkb_run.extend(["--" + option, str(test['options'][option])])
    tests_to_run = ", ".join(tests_to_run)
    pkb_run.extend(["--benchmarks", tests_to_run])
    pkb_run.extend(["--json_path", results_location + '/results.json'])
    return pkb_run

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execute tests on indicated cloud platforms')
    parser.add_argument('--cloud', required=True, nargs='+',
            choices=['AWS','gcp','rackspace','azure','openstack'],
            help='The cloud service providers you wish to test on')
    parser.add_argument('--tests', required=True, nargs='+',
            choices=['all', 'iperf','fio','ping','coremark','unixbench'],
            help='The tests that we have certified for use against the clouds')
    parser.add_argument('--config_file', default='../etc/config_file.yaml',
            nargs='?', help='The configuration file for the tests that we will use')
    parser.add_argument('--dryrun', action='store_true', help='Dry run the tests')
    args = parser.parse_args()
    main()

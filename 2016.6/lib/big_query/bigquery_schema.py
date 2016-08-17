#!/usr/bin/python

'''
Written by: David Kheyman

Adapted from script written by Daniel Cook
All credit goes to him, I just modified this to be a JSON delineator instead

Original code:
https://gist.github.com/danielecook/3175c578c8a0118ead35

'''

import mimetypes
import sys, os
import argparse, json, re, pprint
from collections import OrderedDict

pp = pprint.PrettyPrinter(depth=6)

class BigQueryMaker:

    def __init__(self):
        return

    def create_schema(self, filename, cloud, tests, debug=None):
        if self.file_type(filename) != 'application/json':
            raise TypeError("Filename '{0}' is not valid; must be json".format(filename))
        else:
            if tests == 'all':
                tests = ['fio', 'ping', 'iperf', 'unixbench', 'coremark']
            readfile = open(filename,'r')
            table_schema = {}
            for json_line in readfile:
                decoded_json = self.decode_json(json_line)
                if (decoded_json['test'] in tests):
                    tests.remove(decoded_json['test'])
                    table_schema = self.assign_types(decoded_json)
                    if (debug == True):
                        pp.pprint(table_schema)
                    directory = os.pardir + '/lib/providers/' + cloud + '/schema/'
                    self.create_dir(directory)
                    filename = 'table_' + decoded_json['test'] + '.json'
                    self.file_write(table_schema, directory, filename)
                else:
                    next

    def file_type(self, filename):
        type = mimetypes.guess_type(filename)
        return type[0]

    def create_dir(self, directory):
        if not os.path.isdir(directory):
            os.umask(022)
            os.makedirs(directory)
            os.chown(directory, os.getuid(), -1)
        else:
            return

    def file_write(self, table_schema, directory, filename):
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = directory + filename
        with open(filepath, 'w') as outfile:
            encoded_json = json.JSONEncoder().encode(table_schema)
            outfile.write(encoded_json)

    def decode_json(self, json_line):
        data = None
        try:
            data = json.JSONDecoder().decode(json_line)
        except:
            raise Exception("JSON is not decodable in the file presented")
            sys.exit(1)
        return data

    def determine_type(self, value):
        if (value == None):
            return "STRING"
        else:
            if (isinstance(value, int) and value != 0):
                return "FLOAT"
            elif (isinstance(value, float)):
                return "FLOAT"
            elif (isinstance(value, int) and value == 0):
                return "BOOLEAN"
            elif (isinstance(value, str)):
                return "STRING"
            elif (isinstance(value, list)):
                return "RECORD"
            else:
                return "STRING"


    def assign_types(self, json_struct):
        if (json_struct == None):
            raise Exception("JSON structure cannot be None")
            return
        data_list = []
        for elem_name, elem_value in dict.iteritems(json_struct):
            schema_row = {}
            if (isinstance(elem_value, dict)):
                '''
                If we are dealing with a nested JSON, proceed like so
                '''
                bq_type = "RECORD"
                inner_schema = self.assign_types(elem_value)
                schema_row["fields"] = inner_schema
            else:
                bq_type = self.determine_type(elem_value)
            schema_row["name"] = elem_name
            schema_row["type"] = bq_type
            data_list.append(schema_row)
        return data_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create bigquery schema for results files')
    parser.add_argument('--results_file', required=True, metavar='', nargs='?',
                    help='Created results file of a test; must be a json format')
    parser.add_argument('--debug', default=False, nargs='?',
                    help='Prints out to screen the json bigquery schema')
    parser.add_argument('--cloud', required=True, nargs='+',
                    choices=['AWS', 'Rackspace', 'Azure', 'GCP', 'Openstack'],
                    help='The cloud service provider which was used to run the test against')
    parser.add_argument('--tests', required=True, nargs='+',
                    choices=['fio','unixbench','coremark','iperf','ping', 'all'],
                    help='The tests for which we are writing the schema')
    args = parser.parse_args()
    schema_maker = BigQueryMaker()
    create_schema(args.results_file, args.cloud, args.tests, args.debug)


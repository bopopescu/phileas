#!/usr/bin/python
import sys
sys.path.append('../lib')
from big_query.bigquery_object import BigQueryObject
import json, pprint

if __name__ == '__main__':
    bq = BigQueryObject('phileas-1351')
    bq.create_dataset('trial3', 'description')

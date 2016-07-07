#!/usr/bin/python
from oauth2client.client import GoogleCredentials
#from googleapiclient.discovery import build
from bigquery import get_client
import json, pprint

class BigQueryObject(object):

    def __init__(self, projectId):
        self.credentials = GoogleCredentials.get_application_default()
        self.client = get_client(projectId, credentials=self.credentials)

    def check_dataset(self, datasetId):
        return self.client.check_dataset(datasetId)

    def create_dataset(self, datasetId, description):
        return self.client.create_dataset(datasetId, friendly_name=datasetId, description=description)

    def get_dataset(self, datasetId):
        return self.client.get_dataset(datasetId)

    def create_table(self, datasetId, tableId, schema):
        handle = open(schema, 'r')
        assert handle is not None
        decoder = json.JSONDecoder()
        json_schema = handle.read()
        schema = decoder.decode(json_schema)
        return self.client.create_table(datasetId, tableId, schema)

    def check_table(self, datasetId, tableId):
        return self.client.check_table(datasetId, tableId)

    def add_data_to_table(self, datasetId, tableId, data_loc):
        handle = open(data_loc, 'r')
        assert handle is not None
        data_rows = []
        decoder = json.JSONDecoder()
        for json_line in handle:
            data = decoder.decode(json_line)
            if tableId == data['test']:
                data_rows.append(data)
            else:
                next
        return self.client.push_rows(datasetId, tableId, data_rows)


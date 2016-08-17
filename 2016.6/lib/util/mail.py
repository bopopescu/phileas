#!/usr/bin/python

from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build
from googleapiclient import errors
import httplib2, mimetypes, os
import base64
import logging
from time import strftime, gmtime
from os.path import basename
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


'''
This classs came almost directly from the Google Gmail API
as a means to fetch the credentials we have
for the project on the google API page
'''

class Mailer(object):

    def __init__(self, email_list, email_sender):
        assert(isinstance(email_list, list))
        assert(email_sender)
        self.mailing_list = email_list
        self.credentials = self.get_credentials()
        self.setup_service()
        self.setup_mailer(email_sender)

    def get_credentials(self):
        '''
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'gmail-python-quickstart.json')
        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            credentials = tools.run_flow(flow, store)
            print('Storing credentials to ' + credential_path)
        '''
        credentials = GoogleCredentials.get_application_default()
        return credentials

    def setup_service(self):
        self.service = build('gmail', 'v1', credentials=self.credentials)
        logging.info(self.service)

    def setup_mailer(self, email_sender):
        self.mailer = MIMEMultipart()
        self.mailer["To"] = ','.join(self.mailing_list)
        self.mailer["From"] = email_sender
        self.mailer["Subject"] = "Phileas Run " + strftime("%a, %d %b %Y %H:%M:%S", gmtime())
        msg = MIMEText("These are the latest phileas execution results")
        self.mailer.attach(msg)


    def attach_files(self, file_list):
        assert(file_list)
        for filename in file_list:
            print filename
            assert(os.path.isfile(filename))
            ctype, encoding = mimetypes.guess_type(filename)
            maintype, subtype = ctype.split('/', 1)
            if (subtype == 'csv' or subtype == 'json'):
                with open(filename, 'rb') as fp:
                    msg = MIMEBase(maintype, subtype)
                    msg.set_payload(fp.read())
                encoders.encode_base64(msg)
            else:
                with open(filename, 'rb') as fp:
                    msg = MIMEText(fp.read(), _subtype=subtype)
            msg.add_header('Content-Disposition', 'attachment', filename=filename)
            self.mailer.attach(msg)

    def email_attachments(self):
        try:
            message = {'raw': base64.urlsafe_b64encode(self.mailer.as_string())}
            sent = (self.service.users().messages().send(userId="me", body=message).execute())
            print 'Message Id: %s' % sent['id']
            return sent
        except errors.HttpError, error:
            print 'An error occurred: %s' % error



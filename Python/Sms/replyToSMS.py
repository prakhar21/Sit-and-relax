#!/usr/bin/env python
#@uthor: Prakhar

# importing packages
from twilio.rest import TwilioRestClient
import sys
import os
import subprocess
from prettytable import PrettyTable

try:
	os.system('sh install_dependencies.sh')
	os.system('source ~/.bashrc')
	print 'Environment is set.'
except Exception as e:
	print e
	sys.exit()


# Information is set in environment
try:
	ACCOUNT_SID = os.environ.get('Twilio_Sid')
	AUTH_TOKEN = os.environ.get('Twilio_Token')
	PHONE_TO = os.environ.get('Phone_To')
	PHONE_FROM = os.environ.get('Phone_From')
except Exception as KeyError:
	print '\nEnvironment variables are not set properly'
	sys.exit()



def getClient(a_sid,a_token):
	try:
		client = TwilioRestClient(a_sid, a_token)
	except Exception as e:
		print 'Wrong Credentials\n'
		sys.exit()
	return client

# Caller details
sms_text = ""

# Display the settings
table = PrettyTable(["Setting", "Value"])
table.add_row(["Twilio Sid", ACCOUNT_SID])
table.add_row(["Twilio Token", AUTH_TOKEN])
table.add_row(["Calling to", PHONE_TO])
table.add_row(["My number", PHONE_FROM])
print table


client = getClient(ACCOUNT_SID,AUTH_TOKEN)

try:
	client.messages.create(to=PHONE_TO,from_=PHONE_FROM,body=sms_text,)
except Exception as e:
	print e
	sys.exit()


print 'Done\n'
sys.exit()


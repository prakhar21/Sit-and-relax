#@uthor: Prakhar

# Import packages
from twilio.rest import TwilioRestClient
import sys
import subprocess
import os
import twilio.twiml
from bs4 import BeautifulSoup


try:
	os.system('sh install_dependencies.sh')
	os.system('source ~/.bashrc')
	print 'Environment is set.'
except Exception as e:
	print e
	sys.exit()


# Username and Passwords are set in environment
try:
	ACCOUNT_SID = os.environ.get('Twilio_Sid')
	AUTH_TOKEN = os.environ.get('Twilio_Token')
	PHONE_TO = os.environ.get('Phone_To')
	PHONE_FROM = os.environ.get('Phone_From')
except Exception as KeyError:
	print '\nEnvironment variables are not set properly.\n'
	sys.exit()



def makeCall(u,PHONE_TO,PHONE_FROM):
	
	try:
		client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
		call = client.calls.create(to=PHONE_TO, from_=PHONE_FROM,
						url="http://twimlets.com/echo?Twiml=<Response><Say>"+str(u)+"</Say></Response>"
					  )
		return 'success'
	except Exception as e:
		return e


def tryOnLocalhost():
	pass

#print ACCOUNT_SID, AUTH_TOKEN, PHONE_TO, PHONE_FROM
# Message to speak
message_to_say = "<message to speak out>"


# Makes call
resp = makeCall(message_to_say, PHONE_TO,PHONE_FROM)

if resp != 'success':
	sys.exit()
else:
	print 'url request is down'

	if tryOnLocalhost():
		sys.exit()
	else:
		print 'localhost not working'
		sys.exit()



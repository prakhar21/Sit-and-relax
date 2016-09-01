#@uthor: Prakhar

# importing packages
from twilio.rest import TwilioRestClient
import sys
import os

# credentials
ACCOUNT_SID = "<Enter you SID>" 
AUTH_TOKEN = "<Enter your TOKEN>" 
 
def getClient(a_sid,a_token):
	try:
		client = TwilioRestClient(a_sid, a_token)
	except Exception as e:
		print 'Wrong Credentials\n'
		sys.exit()
	return client

# Caller details
send_to = "" # sender number
send_from = "" # twilio number
sms_text = "Hi"

client = getClient(ACCOUNT_SID,AUTH_TOKEN)

try:
	client.messages.create(to=send_to,from_=send_from,body=sms_text,)
except Exception as e:
	print e
	sys.exit()


print 'Done\n'
sys.exit()


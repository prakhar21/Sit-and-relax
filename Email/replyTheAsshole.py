#@uthor: Prakhar

# Load Packages
import gmail
import os
import sys
import subprocess
import re


try:
	subprocess.call('source ~/.bashrc', shell=True)
	print 'Environment is set.'
except Exception as e:
	print e
	sys.exit()

# Username and Passwords are set in environment
try:
	GMAIL_USER_ID = os.environ.get('Gmail_ID')
	GMAIL_USER_PASSWD = os.environ.get('Gmail_Password')
except Exception as KeyError:
	print '\nEnvironment variables are not set properly.\n'
	sys.exit()


def loginToGmail(u,p):
	# Login to your gmail account
	try:
		g = gmail.login(u, p)
	except Exception as e:
		print '\nSomething messed up\n'
	return g


g = loginToGmail(GMAIL_USER_ID, GMAIL_USER_PASSWD)

# You should write your name here, because this would be of help in filtering out all common work mails from the one in-which you are mentioned
regex_search_keywords_01 = "" 


# Check if Logged in or not
if g.logged_in:
	print '\nSuccessful Login.\n'
	
	sender = ["sender-id"]

	for s in sender:
		mails =  g.inbox().mail(unread = True, sender = s)
	
		# Loop through unread mails sent by boss 
		for mail in mails:
			# Access the body of the mail
			mail.fetch()
			body = mail.body
			
			# Matches the regex and accordingly adds start and labels the mail
			if re.search(regex_search_keywords_01, str(body)):
				mail.star()
				mail.add_label("Interest Match")

else:
	print '\nLogin Failed.\n'


# Logout
print '\nLogging Out.\n'
g.logout()
sys.exit()

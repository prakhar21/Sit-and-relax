#@uthor: Prakhar

# Load Packages
import os
import subprocess
import easygui
import time
import sys
import talkey

remindAgain = False


Message = "It is time to take your pills"

def playMessage(Message):
	try:
		# Voice Feature
		tts = talkey.Talkey(
					preferred_languages=['en'],
					preferred_factor=80.0,
				    	engine_preference=['espeak']
			   	   )
		tts.say(Message)
	except Exception as e:
		return 0

	return 1

if playMessage(Message):
	# Prompts for the first time
	response_01 = easygui.msgbox('Take your medicines. Else you will be bald one day !!','BATRA MEDICINES')
else:
	sys.exit()

if response_01 == 'OK':
	remindAgain = True


#Reminds again
def remindMe():
	response_02 = easygui.ynbox('Did you take your medicines ?', 'REMINDER', ('Yes','No'))
	
	if response_02:
		return 1
	else:
		time.sleep(3)
		remindMe()

if remindAgain:
	time.sleep(3)
	responseFinal = remindMe()

	if responseFinal:
		sys.exit()
	
	

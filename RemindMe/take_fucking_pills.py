#@uthor: Prakhar

# Load Packages
import os
import subprocess
import easygui
import time

remindAgain = False


# Prompt for the first time
response_01 = easygui.msgbox('Take your medicines. Else you will be bald one day !!','BATRA MEDICINES')

if response_01 == 'OK':
	remindAgain = True


# Reminds again
def remindMe():
	response_02 = easygui.ynbox('Did you take your medicines ?', 'REMINDER', ('Yes','No'))
	
	if response_02:
		return 1
	else:
		time.sleep(300)
		remindMe()

if remindAgain:
	time.sleep(300)
	responseFinal = remindMe()

	if responseFinal:
		sys.exit()
	
	

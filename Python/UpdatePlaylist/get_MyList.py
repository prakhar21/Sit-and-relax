#`!/usr/bin/env python

'''
@uthor: Prakhar Mishra
'''

import sys
import pafy
import subprocess
import argparse
from prettytable import PrettyTable
import os
import string
import re


def setEnvironment():
	try:
		os.system('sh install_dependencies.sh')
		os.system('source ~/.bashrc')
	except Exception as e:
		print e
		sys.exit()


def getLinkLocation():
	try:
		LINK = os.environ.get('Playlist_Location')
		print LINK
	except Exception as e:
		print e
		sys.exit()

	return LINK


def makeDirectoryForStorage():
	try:
		if os.path.isdir('Videos/') and os.path.isdir('Audios/'):
			pass
		else:
			os.system('mkdir Videos')
			os.system('mkdir Audios')

		return 1

	except Exception as e:
		return 0


def convertToMp3():
	a= []

	for song in os.listdir('.'):
		a.append(song)
	
	for i in a:
		try:
			os.system('pacpl --to mp3 ' + str(i))
		except Exception as e:
			print '\nFailed in conversion'
			return 0
	
	try:
		# move to audio folder
		os.system('mv *.mp3 ../Audios/')
	except Exception as e:
		print '\nFailed to move'
		return 0

	return 1


# Checks if phone is connected to the system
def viaUSB(usb_tokens):
	print 'via usb'
	connected_devices = subprocess.check_output('lsusb',shell=True)
	connected_devices = connected_devices.split('\n')
	regex_extract_id = "ID\s*(\S+?:\S+)"

	print usb_tokens
	# Get the list of token for connected devices
	id_list = []
	for device in connected_devices:
		connected_devices_ids = re.findall(regex_extract_id,device)
		id_list.append(connected_devices_ids)

	id_list_n = [i[0] for i in id_list if len(i) > 0]
	id_list_nw = list(set(id_list_n))
	
	# Check for existance
	if usb_tokens in id_list_nw:
		# Mobile is connected
		return 1
	else:
		return 0
	

def viaBLUETOOTH():
	pass


def viaWIFI():
	pass


def transferAudio():
	try:
		os.chdir('../Audios/')
		for song in os.listdir('.'):
			os.system('sudo cp ' +str(song) + ' /media/prakhar/')
		return 1
	except Exception as e:
		print e
		return 0
		

def checkForPhoneConnection(usb_t):
	print 'checking'
	if viaUSB(usb_t):
		print '\nMobile is connected by usb'
		transferAudio()
		sys.exit()
	elif viaBLUETOOTH():
		print '\nMobile is connected by bluetooth'
		#transferAudio()
	elif viaWIFI():
		print '\nMobile is connected by wifi'
		#transferAudio()
	else:
		return 0

	return 1


def runtasks(LINK,usb_t):

	if makeDirectoryForStorage():
		pass
	else:
		'Directory does not exist\n'
		sys.exit()

	try:
		os.chdir('Videos/')
		playlist = pafy.get_playlist(LINK)
	
		no_of_songs = len(playlist['items'])
		#print no_of_songs
		song_downloadable_link = []
	
		# loop through songs and fetch their URL
		for song_id in range(0,no_of_songs-1):
			song_attributes = playlist['items'][song_id]['pafy'].getbest()
			song_attributes.download()
			
		# Renaming the files
		for f in os.listdir('.'):
			new_file_temp = re.sub('[\(\)\-\'\|]','',f)
			new_file_name = new_file_temp.replace(' ','')
			os.rename(f,new_file_name)
	
		if convertToMp3():
			print 'Success in mp3 conversion'
		else:
			return 0
		
		if checkForPhoneConnection(usb_t):
			print 'Connection found\n'
		else:
			print 'Mobile not connected\n'
			return 0

	except Exception as e:
		print 'Unable to Fetch Songs\n'
		return 0
	
	return 1
		
if __name__ == '__main__':
	setEnvironment()
	
	parser = argparse.ArgumentParser()

	parser.add_argument('-u', action='store', dest='usb_tokens', help='Stores the port and id for USB device')
	results = parser.parse_args()


	LINK_LOC = getLinkLocation()	

	if runtasks(LINK_LOC,results.usb_tokens):
		print 'Successful Exit...'
		sys.exit()
	else:
		sys.exit()
	

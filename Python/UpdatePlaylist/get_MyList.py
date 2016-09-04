#!/usr/bin/env python

'''
@uthor: Prakhar Mishra
'''

import sys
import pafy
import subprocess
import argparse
from prettytable import PrettyTable
import os


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
		os.system('mkdir Videos')
		return 1
	except Exception as e:
		return 0

def runtasks(LINK):

	if makeDirectoryForStorage():
		pass
	else:
		'Directory does not exist\n'
		sys.exit()

	try:
		os.chdir('Videos/')
		playlist = pafy.get_playlist(LINK)
	
		no_of_songs = len(playlist['items'])

		song_downloadable_link = []
	
		# loop through songs and fetch their URL
		for song_id in range(0,no_of_songs-1):
			song_attributes = playlist['items'][song_id]['pafy'].getbest()
			song_attributes.download()
	
		os.chdir('..')

		return 1

	except Exception as e:
		print 'Unable to Fetch Songs\n'
		return 0
		
if __name__ == '__main__':
	setEnvironment()

	LINK_LOC = getLinkLocation()	

	if runtasks(LINK_LOC):
		print 'Successful Exit...'
		sys.exit()
	else:
		sys.exit()


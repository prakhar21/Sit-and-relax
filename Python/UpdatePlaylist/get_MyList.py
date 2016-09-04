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
	except Exception as e:
		print e
		sys.exit()

	return LINK


def runtasks(LINK):
	playlist = pafy.get_playlist(URL)
	
	no_of_songs = len(playlist['items'])

	song_downloadable_link = []
	# loop through songs and download best ones
	for song_id in xrange(,no_of_songs):
		song_attributes = playlist['items'][song_id]['pafy']
		song_downloadable_link.append(song_attributes.getbest().url)

	return song_downloadable_link

if __name__ == '__main__':
	setEnvironment()
	LINK_LOC = getLinkLocation()	
	runtasks(LINK_LOC)
	print 'Exiting...'
	sys.exit()


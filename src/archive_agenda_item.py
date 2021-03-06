import os
import config

import sys, argparse
import time
import requests
from selenium import webdriver

"""
TODO: I need to add more debug messages
I need to figure out when archiving fails
"""

def save_agenda_item(url):
	"""
	TODO: I need to figure out when pywb finishes loading
	"""
	driver = webdriver.Chrome()

	try:
		driver.get(config.RECORD_URL + "/" + url)
		time.sleep(20)
		driver.close()
		return True
	except:
		print( "Saving url failed : " + url, file=sys.stderr)
		return False
	
	


def main(argv):
	parser = argparse.ArgumentParser(description="Archive Agenda ID to warc file \n" +
		"If only the url is inputted, then the url is fetched \n" +
		"If only the id is passed then this url is used " + config.AGENDA_ID_URL + "\n" +
		"If both the id and url is passed, the url is fetch in this format \n" + 
		"https://url.domain?ID={} ID replaces the braces"
	)
	parser.add_argument('--id', nargs='?', help='Agenda Meeting ID to archive')
	parser.add_argument('url', nargs='?', help='Meeting ID URL')
	options = parser.parse_args(argv)

	url_options = 0
	if options.id is not None:
		url_options |= 1
	if options.url is not None:
		url_options |= 2
	
	meeting_url = ""
	if url_options is 1:
		meeting_url = config.AGENDA_ID_URL + options.id
	elif url_options is 2:
		meeting_url = options.url
	elif url_options is 3:
		meeting_url = options.url.format(options.id)
	config.initalize_record()
	save_agenda_item(meeting_url)
	config.terminate()


if __name__ == "__main__":
	config.initalize_project_root()
	main(sys.argv[1:])
	



	

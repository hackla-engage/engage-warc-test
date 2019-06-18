import os
import config

import sys, argparse


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


if __name__ == "__main__":
	config.initalize_project_root()
	main(sys.argv[1:])
	



	

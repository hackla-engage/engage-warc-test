import config
import urllib.request
import sys
import traceback

import requests

import generate_urls
import parse_agenda_item

if __name__ == "__main__":
	config.initialize()
	for archive_url in generate_urls.generateURL():
		try:
			with requests.get(archive_url.get_wayback_url()) as response:
				print(response.text)
		except Exception as error:
			traceback.print_exc()
			print("Error url fetch failed: " + archive_url.get_wayback_url(), file=sys.stderr)
	config.terminate()
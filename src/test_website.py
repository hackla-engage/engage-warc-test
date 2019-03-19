import config
import urllib.request
import sys
import traceback

import requests

from generate_urls import ArchiveUrl
from generate_urls import generateURL


if __name__ == "__main__":
	config.initialize()
	for archive_url in generateURL():
		try:
			with requests.get(archive_url.get_wayback_url()) as response:
				print(response.text)
		except Exception as error:
			traceback.print_exc()
			print("Error url fetch failed: " + archive_url.get_wayback_url(), file=sys.stderr)
	config.terminate()
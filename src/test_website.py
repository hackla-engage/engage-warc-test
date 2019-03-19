import config
import urllib.request
import sys

from generate_urls import ArchiveUrl
from generate_urls import generateURL


if __name__ == "__main__":
	config.initialize()
	for archive_url in generateURL():
		try:
			with urllib.request.urlopen(archive_url.get_wayback_url()) as response:
				print(response.read())
		except:
			print("Error url fetch failed: " + archive_url.get_wayback_url(), file=sys.stderr)
	config.terminate()
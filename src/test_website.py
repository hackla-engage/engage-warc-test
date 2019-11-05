from __future__ import absolute_import
from engage_scraper.scraper_logics.santamonica_scraper_logic import SantaMonicaScraper
from urllib.parse import urlparse
from bs4 import BeautifulSoup

import config
import urllib.request
import sys
import traceback

import requests

import generate_urls
import argparse


if __name__ == "__main__":
	
	config.initialize()
	for archive_url in generate_urls.generateURL():
		try:
			
			#with requests.get(archive_url.get_wayback_url()) as response:
				#print(archive_url.url)
				#print(response.text)
		except Exception as error:
			traceback.print_exc()
			print("Error url fetch failed: " + archive_url.get_wayback_url(), file=sys.stderr)
	config.terminate()
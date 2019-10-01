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
import parse_agenda_item

import argparse


if __name__ == "__main__":
	
	config.initialize()
	archive_url = generate_urls.get_agenda_item_archive(3610)
	try:
		#print(archive_url)
		with requests.get(archive_url.get_wayback_url()) as response:
			bs4 = BeautifulSoup(response.text, 'html.parser')
			print(parse_agenda_item.parse_agenda_item(bs4, 3610))
	except Exception as error:
			traceback.print_exc()
			print("Error url fetch failed: " + archive_url.get_wayback_url(), file=sys.stderr)
	config.terminate()
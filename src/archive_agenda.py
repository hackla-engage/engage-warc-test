import os
import config
from bs4 import BeautifulSoup
import functools
import traceback

import datetime
from warcio.warcwriter import WARCWriter
from warcio.statusandheaders import StatusAndHeaders
import requests

def parse_session(html, year):
	soupget = BeautifulSoup(html, 'html.parser')
	form = soupget.find('form', {'name': 'aspnetForm'})
	formInputs = form.findChildren('input')
	payload = dict()
	for input in formInputs:
		if input.get('name') in ["EktronClientManager", "__VIEWSTATE", "__VIEWSTATEGENERATOR", "__EVENTVALIDATION"]:
			payload[input.get('name')] = input.get('value')
	payload["ctl00$ctl00$bodyContent$mainContent$ddlYears"] = str(year)
	return payload

def post_url(url, headers):
	return url + '?' + functools.reduce(lambda acc, k: acc + '&' + k + '=' + headers[k] , headers.keys())
		

if __name__ == "__main__":
	config.initalize_project_root()
	today = datetime.date.today()
	#config.initalize_record()
	r = requests.get( config.AGENDA_URL)
	session_headers = parse_session(r.text, 2018)
	
	with open(  'rec-' + today.strftime("%Y%m%d%H%M%S") + '-psuedos-MacBook-Pro.local.warc.gz', 'wb') as output:
		writer = WARCWriter(output, gzip=True)
		response = requests.post(config.AGENDA_URL, data=session_headers)
		headers_list = response.raw.headers.items()
		http_headers = StatusAndHeaders('200 OK', headers_list, protocol='HTTP/1.0')
		record = writer.create_warc_record(config.AGENDA_URL, 'response', payload=response.raw, http_headers=http_headers)
		writer.write_record(record)
	

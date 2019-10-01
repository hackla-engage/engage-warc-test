#!/usr/bin/env python

import warc
import os, sys
import config
from datetime import datetime

from urllib.parse import urlparse 
import re
# type(f) = warc.warc.WARCFile
# type(record) = warc.warc.WARCRecord
# vars(warc.warc.WARCRecord) = {'header': <WARCHeader: type='response', record_id='<urn:uuid:45f3f82c-446d-11e9-b1c6-784f43777a5e>'>, 'payload': <warc.utils.FilePart object at 0x104a12128>, '_content': None}
# type(warc.warc.WARCRecord.header) = <class 'warc.warc.WARCHeader'>

class ArchiveUrl:
	def __init__(self, u, r_id, d, file):
		self.url = u
		self.record_id = r_id
		self.datetime = datetime.strptime(d, '%Y-%m-%dT%H:%M:%SZ')
		self.filename = file

	def get_filename(self):
		return self.filename

	def get_wayback_url(self):
		"""
		This function generates the wayback url when the wayback server is running
		Sample framed url: http://localhost:8080/smgov/20190312021930/https://www.smgov.net/departments/clerk/agendas.aspx
		Sample frameless url: http://localhost:8080/smgov/20190129033819mp_/https://www.smgov.net/departments/clerk/agendas.aspx
		frame url doc:  https://pywb.readthedocs.io/en/latest/manual/configuring.html#framed-vs-frameless-replay
		"""
		return config.SERVER + '/' + config.COLLECTION_NAME + '/' + self.datetime.strftime('%Y%m%d%H%M%S') + 'mp_'  + '/' + self.url

	def is_agenda_item(self):
		"""
		All agenda items has the same format. 
		http://santamonicacityca.iqm2.com/Citizens/Detail_Meeting.aspx?ID=####
		Example: http://santamonicacityca.iqm2.com/Citizens/Detail_Meeting.aspx?ID=1199

		Just do a simple regex match. I can technically create a parser to grab the ID
		"""
		prog = re.compile('.*//santamonicacityca.iqm2.com/Citizens/Detail_Meeting.aspx?.*')
		return prog.match(self.url) is not None
"""
This funtion generates all the ArchiveURLs
"""
def generateURL():
	warc_files = os.listdir(config.COLLECTIONS_PATH)
	for f_name in warc_files:
		if f_name == "_warc_cache": # Apparently warc modules makes its own cache directory _warc_cache
			continue
		f = warc.open( config.COLLECTIONS_PATH + str(f_name))
		for record in f:
			yield ArchiveUrl( record['WARC-Target-URI'],record['WARC-Record-ID'],record['WARC-Date'],f_name ) #we only need the first record.
			break

def check_agenda_id(archive_url, num):
	parse_result = urlparse( archive_url.url )
	if( "santamonicacityca.iqm2.com" == parse_result.netloc and "/Citizens/Detail_LegiFile.aspx" == parse_result.path):
		tokens = parse_result.query.split("&")
		if "ID=" + str(num) in tokens:
			return True
		else:
			return False

def get_agenda_item_archive(num):
	for archive_url in generateURL():
		if (check_agenda_id(archive_url, num)):
			return archive_url
	return None
		

if __name__ == "__main__":
	for url in generateURL():
		print("url: " + url.get_wayback_url() + ",is_agenda_item: " + str(url.get_filename()) )
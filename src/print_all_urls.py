#!/usr/bin/env python

import warc
import os
import config

# type(f) = warc.warc.WARCFile
# type(record) = warc.warc.WARCRecord
# vars(warc.warc.WARCRecord) = {'header': <WARCHeader: type='response', record_id='<urn:uuid:45f3f82c-446d-11e9-b1c6-784f43777a5e>'>, 'payload': <warc.utils.FilePart object at 0x104a12128>, '_content': None}
# type(warc.warc.WARCRecord.header) = <class 'warc.warc.WARCHeader'>

if __name__ == "__main__":
	warc_files = os.listdir(config.COLLECTIONS_PATH)
	for f_name in warc_files:
		f = warc.open( config.COLLECTIONS_PATH + str(f_name))
		for record in f:
			print( ",".join([ record['WARC-Target-URI'],record['WARC-Record-ID'],record['WARC-Date'] ])  ) #we only need the first record. 
			break
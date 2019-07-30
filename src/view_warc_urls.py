# python3 src/view_warc_urls.py rec-20190709023517365419-psuedos-MacBook-Pro.local.warc.gz

import warc
import os, sys
import config
import argparse
from datetime import datetime

import re

def dumpfile(file):		
	f = warc.open( config.COLLECTIONS_PATH + str(file))
	for record in f:
		print( "%s,%s,%s"% (record['WARC-Target-URI'],record['WARC-Record-ID'],record['WARC-Date']) ) #we only need the first record.
			


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("filename", help="Enter warch filename")
	args = parser.parse_args()
	dumpfile(args.filename)

	
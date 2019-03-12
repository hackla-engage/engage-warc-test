#!/usr/bin/env python

import warc
import os


COLLECTIONS_DIR = '../collections/smgov/archive/'

if __name__ == "__main__":
	warc_files = os.listdir(COLLECTIONS_DIR)
	for f_name in warc_files:
		f = warc.open( COLLECTIONS_DIR + str(f_name))
		for record in f:
			print( record['WARC-Target-URI'] )
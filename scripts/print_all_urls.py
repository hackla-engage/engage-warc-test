#!/usr/bin/env python

import warc
import os


COLLECTIONS_DIR = "../collections/smgov/archive"

if __name__ == "__main__":
	warc_files = os.listdir(COLLECTIONS_DIR)
	print(warc_files)
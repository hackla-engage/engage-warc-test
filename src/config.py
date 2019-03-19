import os
import subprocess

PROJECT_ROOT = os.path.realpath(__file__ + "/../../")

COLLECTIONS_PATH = PROJECT_ROOT + '/collections/smgov/archive/'

COLLECTION_NAME = 'smgov'
SERVER = 'localhost:8080'

def initialize():
	global _wayback_process
	os.chdir(PROJECT_ROOT) #chroot to project root dir
	_wayback_process = subprocess.Popen(["wayback"]) #start wayback machine

def terminate():
	_wayback_process.kill()

import os
import subprocess
import time

PROJECT_ROOT = os.path.realpath(__file__ + "/../../")

COLLECTIONS_PATH = PROJECT_ROOT + '/collections/smgov/archive/'

COLLECTION_NAME = 'smgov'
SERVER = 'http://localhost:8080'

AGENDA_URL = 'https://www.smgov.net/departments/clerk/agendas.aspx'

def initialize():
	global _wayback_process
	os.chdir(PROJECT_ROOT) #chroot to project root dir
	_wayback_process = subprocess.Popen(["wayback"]) #start wayback machine
	time.sleep(5)

def terminate():
	_wayback_process.kill()

def initalize_process():
	global _wayback_process
	os.chdir(PROJECT_ROOT)
	_wayback_process = subprocess.Popen(["wayback", "--record", "--live", "-a"])
	time.sleep(5)

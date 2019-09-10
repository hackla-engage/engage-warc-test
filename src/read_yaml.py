import config
import os
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class TestBase:
	def __init__(self, unix_time, archive_uuid, url, id):
		self.archive_uuid = archive_uuid
		self.unix_time = unix_time
		self.url = url
		self.id = id

class MeetingItemCase(TestBase):
	def __init__(self, unix_time, archive_uuid, url, id):
		super().__init__(
			unix_time=unix_time, 
			archive_uuid=archive_uuid,
			id=id,
			url=url
		)

"""
Todo: Figure out a better way to find meeting id
Algorithm: Linearly open files until proper meeting id found
"""
def read_meeting_id(id):
	meeting_item_files = os.listdir(config.MEETING_ITEM_PATH)
	for file_name in meeting_item_files:
		data = load(open(config.MEETING_ITEM_PATH+"/"+file_name, 'r'), Loader=Loader)
		if data[0]['meeting_id'] == id:
			return MeetingItemCase(
				unix_time=data[0]['meeting_time'],
				archive_uuid=data[0]['archive_uuid'],
				url=data[0]['url'],
				id=id
			)
	


if __name__ == "__main__":
	read_meeting_id(1183)

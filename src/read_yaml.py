import config
import os
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class TestBase:
	def __init__(self, archive_uuid, url, id):
		self.archive_uuid = archive_uuid
		self.url = url
		self.id = id

class MeetingItemCase(TestBase):
	def __init__(self, unix_time, archive_uuid, url, id):
		super().__init__(
			archive_uuid=archive_uuid,
			id=id,
			url=url
		)
		self.unix_time=unix_time
	def to_json(self):
		return {
			"unix_time" : self.unix_time,
			"url" : self.url,
			"id" : self.id,
			"archive_uuid" : self.archive_uuid,
		}

class AgendaItemCase(TestBase):
	def __init__(self, title, department, archive_uuid, url, id):
		super().__init__(
			archive_uuid=archive_uuid,
			id=id,
			url=url
		)
		self.title = title
		self.department = department

	def to_json(self):
		return {
			"department" : self.department,
			"url" : self.url,
			"id" : self.id,
			"archive_uuid" : self.archive_uuid,
			"title" : self.department,
		}


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

def read_agenda_id(id):
	agenda_item_file_names = os.listdir(config.AGENDA_ITEM_PATH)
	for file_name in agenda_item_file_names:
		data = load(open(config.AGENDA_ITEM_PATH+"/"+file_name, 'r'), Loader=Loader)
		if data[0]['agenda_item_id'] == id:
			return AgendaItemCase(
				title=data[0]['title'],
				department=data[0]['department'],
				archive_uuid=data[0]['archive_uuid'],
				url=data[0]['url'],
				id=id
			)	


if __name__ == "__main__":
	read_meeting_id(1183)
	print(read_agenda_id(3610).to_json())

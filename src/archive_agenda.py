import os
import config
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver


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


if __name__ == "__main__":
	http = urllib3.PoolManager()
	r = http.request('GET', config.AGENDA_URL)
	session_headers = parse_session(r.data, 2018)
	agenda_request = http.request('POST', config.AGENDA_URL, fields=session_headers)
	#driver = webdriver.Chrome()
	#driver.get("data:text/html;charset=utf-8,"+r.data)
	f = open('sample.html', 'a')
	print(agenda_request.data)
	f.write(agenda_request.data.decode("utf-8"))
	f.close()
	
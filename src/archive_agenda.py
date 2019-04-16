import os
import config
import urllib3
from bs4 import BeautifulSoup
import functools
import traceback


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

def post_url(url, headers):
	return url + '/post?' + functools.reduce(lambda acc, k: acc + '&' + k + '=' + headers[k] , headers.keys())
		

if __name__ == "__main__":
	config.initalize_record()
	http = urllib3.PoolManager()
	r = http.request('GET', config.AGENDA_URL)
	session_headers = parse_session(r.data, 2018)
	#agenda_request = http.request('POST', config.AGENDA_URL, fields=session_headers)		
	try:
		#https://selenium-python.readthedocs.io/waits.html#explicit-waits
		driver = webdriver.Chrome()
		driver.get(config.RECORD_URL+ '/' + post_url(config.AGENDA_URL, session_headers))
		wait = WebDriverWait(driver, 10)
		wait.until(EC.presence_of_element_located((By.ID, 'title_or_url')))
	except Exception:
		traceback.print_exc()
		driver.close()
		config.terminate()
	driver.close()
	config.terminate()

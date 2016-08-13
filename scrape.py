#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7.10
# pip install requests
# pip install BeautifulSoup4

import requests
from bs4 import BeautifulSoup

def scrape():
	url = 'http://www.cc.gatech.edu/academics/degree-programs/masters/computer-science/specializations'
	
	page_html = requests.get(url).text

	soup = BeautifulSoup(page_html, 'html.parser')

	tables = soup.find_all('table')

	# 12 tables on page, but only 11 specializations
	del tables[11]

	for table in tables:
		print table.text

if __name__ == '__main__':
	scrape()

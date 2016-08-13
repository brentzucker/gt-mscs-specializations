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

	tbodys = soup.find_all('tbody')

	for t in tbodys:
		table_soup = BeautifulSoup(str(t), 'html.parser')
		tr = table_soup.find_all('tr')
		
		# Parse the Specialization Name, Core Classes, and Electives
		name = tr[0].td.h4.string.strip()[len('Specialization in '):]
		core = tr[1]
		electives = tr[2]
		
		print name

if __name__ == '__main__':
	scrape()

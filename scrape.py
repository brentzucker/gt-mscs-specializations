#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7.10
# pip install requests
# pip install BeautifulSoup4

import requests
from bs4 import BeautifulSoup

class Specialization:
	def __init__(self, name):
		self.name = name
		courses = []

def scrape():
	url = 'http://www.cc.gatech.edu/academics/degree-programs/masters/computer-science/specializations'
	page_html = requests.get(url).text
	return page_html

def parse(page_html):
	soup = BeautifulSoup(page_html, 'html.parser')

	tbodys = soup.find_all('tbody')

	for t in tbodys:
		table_soup = BeautifulSoup(str(t), 'html.parser')
		tr = table_soup.find_all('tr')
		
		# Parse the Specialization Name, Core Classes, and Electives
		name = tr[0].td.h4.string.strip()[len('Specialization in '):]
		print name

	#	# Parse Core Classes (Num of req and class numbers)
	#	core = tr[1]
	#	tr1_soup = BeautifulSoup(str(core), 'html.parser')
	#	core_td = tr1_soup.find_all('td')
	#	for child in core_td[1].descendants:
	#		print str(child.strip()
		
		
	#	electives = tr[2]

		# Parse classes
		for row in [tr[1], tr[2]]:
			lis = BeautifulSoup(str(row), 'html.parser').find_all('li')
			for li in lis:
				if li.string != None:
					course_name = li.string
				else:
					# handle random CS 6400 which is embedded in a <p> tag...
					course_name = li.p.string

				c = course_name.split(" ")[:2]
				course_num = ' '.join(c)
				print course_num


if __name__ == '__main__':
	page_html = scrape()
	parse(page_html)

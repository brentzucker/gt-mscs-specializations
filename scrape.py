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
		self.courses = []
		self.core = []
		self.electives = []

def scrape():
	url = 'http://www.cc.gatech.edu/academics/degree-programs/masters/computer-science/specializations'
	page_html = requests.get(url).text
	return page_html

def parse(page_html):
	soup = BeautifulSoup(page_html, 'html.parser')

	tbodys = soup.find_all('tbody')
	
	specializations = []
	for t in tbodys:
		table_soup = BeautifulSoup(str(t), 'html.parser')
		tr = table_soup.find_all('tr')
		
		# Parse the Specialization Name, Core Classes, and Electives
		name = tr[0].td.h4.string.strip()[len('Specialization in '):]
		specialization = Specialization(name)
		print specialization.name

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
				specialization.courses.append(course_num)
		specializations.append(specialization)
	return specializations

def analyze(specializations):
	specialization_pairs = []
	for s1 in specializations:
		for s2 in specializations:
			if s1.name != s2.name:
				pair = {}
				pair['name'] = s1.name + ' ' + s2.name
				pair['common_courses'] = list(set(s1.courses).intersection(set(s2.courses)))
				pair['num_in_common'] = len(pair['common_courses'])
				specialization_pairs.append(pair)

	# Sort by num_in_common
	specialization_pairs.sort(key=lambda x: x['num_in_common'], reverse=True)

	for sp in specialization_pairs:
		print sp['name']
		print sp['num_in_common']
		print sp['common_courses']

if __name__ == '__main__':
	page_html = scrape()
	specializations = parse(page_html)
	analyze(specializations)

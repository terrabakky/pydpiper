#!/usr/bin/env python


import requests

from lxml import html
    
class Scrape:

	def __init__(self,target=None):
		self.response_html = None
		self.target = target
		self.response = None
		self.parsed_body = None
		self.links = None
		self.visited = set()
		if target:
			self.scrape(target)
			self.parse_body()


	def scrape(self, url):
		if url in visited:
			return False
        
		self.response = requests.get(url)
		self.visited.add(url)
		return True
			
	def parse_body(self):
		self.parsed_body = html.fromstring(self.response.text)
		self.links = self.parsed_body.xpath('//a/@href')
        
        


		

	# def clean_links(self):
	# 	links = [link for link in links if link != '#']


x = Scrape('http://uow.edu.au')

print x.response.content

print '##############'

print x.links



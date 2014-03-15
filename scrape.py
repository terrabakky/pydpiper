#!/usr/bin/env python

import requests

from lxml import html
    
class Scrape:
	def __init__(self):
		self.parsed_body = None
		self.links = []
		self.visited = set()
		
	def scrape(self, url):
		print url
		if url in self.visited:
			return False
        
		response = requests.get(url)
		self.visited.add(url)
		self.parse_body(response.text)
			
	def parse_body(self,html_string):
		parsed_body = html.fromstring(html_string)
		new_links = parsed_body.xpath('//a/@href')
		self.links.extend([str(link) for link in new_links])



        
	






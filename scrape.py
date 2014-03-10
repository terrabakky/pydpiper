#!/usr/bin/env python


import requests

from lxml import html

class Scrape:

	def __init__(self,target=None):
		self.response_html = None
		self.target = target
		self.response = None

		if target:
			self.scrape(target)


	def scrape(self, url):
		self.response = requests.get(url)
		self.response
		self.target = url
		return True


	def links(self):
		response_html().xpath('//a/@href')
		return True

	# def clean_links(self):
	# 	links = [link for link in links if link != '#']


x = Scrape('http://uow.edu.au')

print x.response.content
	











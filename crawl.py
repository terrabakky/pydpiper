#!/usr/bin/env python

from scrape import Scrape

scraper = Scrape()

def process(link,scraper=scraper):

	if link in scraper.visited:
		return False

	scraper.scrape(link)

	return scraper.links

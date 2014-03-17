#!/usr/bin/env python
import time
from redis import Redis
from rq import Queue
from crawl import process
from scrape import scrape
import scrape


# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue(connection=redis_conn)

START_LINK = "http://www.google.com"

first_job = process(START_LINK)

links = scrape.links

visited = set()

if first_job:
	for link in links:
		if not link in visited:
			q.enqueue(process,link)
			visited.add(link)

	while True:
		time.sleep(2)

		print "Visited: " + str(visited)
		# print "All Links: " + str(scrape.links)





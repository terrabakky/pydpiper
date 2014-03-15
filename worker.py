#!/usr/bin/env python

from crawl import *
from redis import Redis
from rq import Queue

# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue(connection=redis_conn)

START_LINK = "http://www.google.com"
start = process(START_LINK)


for link in start:
	link = str(link)
	if link.startswith('http://'):
		q.enqueue(process,str(link))

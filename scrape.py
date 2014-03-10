#!/usr/bin/env python


import requests

from lxml import html

response = requests.get('http://coursefinder.uow.edu.au')

# print response.status_code

# print response.headers

# print response.content


# print response.request.headers

parsed_body = html.fromstring(response.text)

print parsed_body.xpath('//a/@href')


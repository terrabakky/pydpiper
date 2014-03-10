#!/usr/bin/env python


import requests

from lxml import html

url = raw_input('URL >> ').strip()
response = requests.get(url)

# print response.status_code

# print response.headers

# print response.content


# print response.request.headers

parsed_body = html.fromstring(response.text)

print parsed_body.xpath('//a/@href')


#!/usr/local/bin/python
# coding: utf8
import json

with open('.shopping_list.json') as data_file:
    data = json.load(data_file)

content = u"\n"
for item in data:
    if not item['complete']:
        content += u"- %s\n" % item['name']

print(content)
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:44:54 2019

@author: Sabeshnav M
"""

from json2xml import json2xml, readfromurl, readfromstring, readfromjson

"""# get the xml from an URL that return json
data = readfromurl("https://dataturks.com/projects/devika.mishra/face_detection")
print(json2xml.Json2xml(data).to_xml())
# get the xml from a json string
data = readfromstring(
    '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
)
print(json2xml.Json2xml(data).to_xml())"""

# get the data from an URL
data = readfromjson("https://dataturks.com/projects/devika.mishra/face_detection")
print(json2xml.Json2xml(data).to_xml())

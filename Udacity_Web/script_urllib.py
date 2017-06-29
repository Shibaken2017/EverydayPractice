#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from xml.dom import minidom


test=urllib2.urlopen("http://www.example.com/")
print test.headers.items()

print test.url


##########################################
contents=urllib2.urlopen("http://www.nytimes.com/services/xml/rss/nyt/GlobalHome.xml").read()

d=minidom.parseString(contents)

print d.getElementsByTagName("item")
print len(d.getElementsByTagName("item"))
#minidom._get_elements_by_tagName_ns_helper()
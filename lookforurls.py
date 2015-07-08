#!/usr/bin/python
import json
import urllib
import urllib.request
import lxml.html
import lxml.html.clean
import time
import os
import os.path
import string
import datetime
import socket
import sys

# def getclosesturl(purl):
#    pass

a = json.loads('{"archived_snapshots":{"closest":{"available":true,"url":"http://web.archive.org/web/20150703202406/http://www.azlyrics.com/","timestamp":"20150703202406","status":"200"}}}')
print(a['archived_snapshots']['closest']['url'])
try:
    print(json.loads('{"archived_snapshots":{}}')['archived_snapshots']['closest']['url'])
except KeyError as e:
    print("{0}".format(e))
except Exception as e:
    print("Unexpected error:", sys.exc_info()[0])

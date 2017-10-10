#! /usr/bin/env python
import json
import re
import urllib
import sys
import os
import time
from sys import argv
from datetime import datetime
from pytz import timezone

def checktz(pop):
    for z in range(0,len(airport)):
        if pop.upper() in airport[z]["airport_code"]:
                return airport[z]["tz_code"]
                
if len(argv)!=1:
    pop = argv[1]
    path=str(sys.path[0])+"/airport.json"
    json_data=None
    try:
        with open(path) as reader:
            json_data = reader.read()
    except:
        print "Error, can't read airport data json file."
        sys.exit(1)
    airport = json.loads(json_data)
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    tz=checktz(pop)
else:
    tz=None
print "Your location time:"+str(datetime.now())
if (tz==None):
    print "Sorry , I can't find this POP or Airport"
else:
    pop_time = datetime.now(timezone(tz))
    print tz+" time: "+pop_time.strftime(fmt)

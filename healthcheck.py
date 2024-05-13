#!/usr/bin/python

import sys
import requests

response = requests.get('http://service-'+ str(sys.argv[1]) + '.example.com')

if response.content.decode() == '["Pong"]':
    print('Success!')
else:
    print('Fail')

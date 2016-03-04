#!/usr/bin/python

import sys
import urllib.request
import urllib.parse

user = '12345678'
key = '123456789azert'

message = sys.stdin.read()
if len(sys.argv) == 2:
  message += sys.argv[1]

params = urllib.parse.urlencode({'user': user, 'pass': key, 'msg': message})
url = "https://smsapi.free-mobile.fr/sendmsg?%s" % params

try:
  req = urllib.request.urlopen(url)
  print('SMS sended.')
except Exception as e:
  if hasattr(e, 'code'):
    if e.code == 400:
      raise Exception('Some parameter is missing.')
    if e.code == 402:
      raise Exception('Too many sms in a short periode.')
    if e.code == 403:
      raise Exception('Service not activated or user/password incorrect.')
    if e.code == 500:
      raise Exception('Try later.')

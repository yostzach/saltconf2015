#!/usr/bin/env python
import sys
import json
import logging

log = logging.getLogger(__name__)

def get_instance_id(message):
    '''Determines action type (launch / terminate), and returns action type and aws instance-id'''
    try:
      bodydict = {}
      mydict = json.loads(message)
      messagebody = mydict['Message']
      bodydict = json.loads(messagebody)
    except Exception, e:  # log error, and carry on
      log.error("Error: %s" % e)
    return bodydict.get('EC2InstanceId', None)

def get_instance_action(message):
    '''Returns the aws instance id'''
    try:
      bodydict = {}
      mydict = json.loads(message)
      messagebody = mydict['Message']
      bodydict = json.loads(messagebody)
    except Exception, e:
      log.error("Error: %s" % e)
    return bodydict.get('Event', None)

def get_body(message):
    try:
      bodydict = {}
      text = message.get_body()
      mydict = json.loads(text)
      messagebody = mydict['Message']
      bodydict = json.loads(messagebody)
    except Exception, e:
      log.error("Error: %s" % e)
    return bodydict.get('Event', None)
    

if __name__ == "__main__":
  filename = sys.argv[1]
  f = open(filename, "r")
  message = f.read()
  print "instance id: %s" % get_instance_id(message)
  print "instance action: %s" % get_instance_action(message)

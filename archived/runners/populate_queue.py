#!/usr/bin/env python
import boto.sqs
import boto.sqs.message

region = 'us-east-1'
queue = 'SqsMinion'


msg1 = open("instance_launch_msg.txt", "r").read()
msg2 = open("instance_termination_msg.txt", "r").read()

conn = boto.sqs.connect_to_region(region)
print "conn = %s" % conn
myq = conn.get_queue(queue)
print "myq = %s" % myq
my_messages = [msg1,msg2]
for m in my_messages:
  m =  boto.sqs.message.Message()
  m.set_body(msg1)
  myq.write(m)

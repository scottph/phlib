#!/usr/bin/env python

import sys, DNS

query = sys.argv[1]

DNS.DiscoverNameServers()

reqObj = DNS.Request()
ans = reqObj.req(name=query, qtype = DNS.Type.ANY)

if not len(ans.answers):
   print "not found"

for item in ans.answers:
   print "%-5s %s" % (item['typename'], item['data'])

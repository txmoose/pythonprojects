#!/usr/bin/env python

import json
import urllib2
import prettytable

username = raw_input("What is your API username? ")
api_key  = raw_input("What is your API key? ")

auth_url = "https://identity.api.rackspacecloud.com/v2.0/tokens"
data     = '{"auth": {"RAX-KSKEY:apiKeyCredentials":{"username":"' + username + '", "apiKey":"' + api_key + '"}}}'
json_header = {'Content-Type': 'application/json'}

req = urllib2.Request(auth_url, data, json_header)
response = urllib2.urlopen(req)
result = response.read()

auth_json = json.loads(result)

token = auth_json.get("access").get("token").get("id")
account = auth_json.get("access").get("token").get("tenant").get("id")

server_url = 'https://dfw.servers.api.rackspacecloud.com/v2/' + account + '/servers/detail'
auth_header = {'X-Auth-Token': token}

req = urllib2.Request(server_url, None, auth_header)
response = urllib2.urlopen(req)
result = response.read()

server_json = json.loads(result)

table = prettytable.PrettyTable(["Server Name", "UUID"])
table.align["Server Name"] = 'l' 
table.padding_width = 1

print "Your DFW servers and UUID's are as follows: "

for i in server_json.get("servers"):
    table.add_row([i.get('name'), i.get('id')])

print table

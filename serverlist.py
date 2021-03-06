#!/usr/bin/env python
"""Simple program to interact with Cloud Servers"""

import json          #working with JSON objects
import urllib2       #working with API endpoints
import prettytable   #printing things pretty

#global header dict for API requests
json_header = {'Content-Type': 'application/json'}

#Function to auth with Cloud Auth API
def authenticate():
    #getting API Username and API Key if not in 
    #~/.credentials (implementing later)
    username = raw_input("What is your API username? ")
    api_key  = raw_input("What is your API key? ")

    #URL Endpoint for Cloud Auth
    auth_url = "https://identity.api.rackspacecloud.com/v2.0/tokens"
    #Data for API request body
    data     = '{"auth": {"RAX-KSKEY:apiKeyCredentials":{"username":"' +\
               username + '", "apiKey":"' + api_key + '"}}}'

    #API request process & returning response as a JSON object
    req = urllib2.Request(auth_url, data, json_header)
    response = urllib2.urlopen(req)
    result = response.read()
    auth_json = json.loads(result)
    return auth_json

#authenticating and getting JSON object
auth_json = authenticate()

#grabbing token and account number from auth_json
token = auth_json.get("access").get("token").get("id")
account = auth_json.get("access").get("token").get("tenant").get("id")

#URLs for each DC
dc_url = {}
for cp in auth_json.get("access").get("serviceCatalog"):
    if cp['name'] == 'cloudServersOpenStack':
        for ep in cp['endpoints']:
            dc_url[ep['region'].lower()] = ep['publicURL']

#header dict for auth token
auth_header = {'X-Auth-Token': token}

#Function to get server list
def serverlist(servers_url, auth_header):
    req = urllib2.Request(servers_url, None, auth_header)
    response = urllib2.urlopen(req)
    result = response.read()
    
    server_json = json.loads(result)
    return server_json

#getting DC from user
print "Which DC do you want servers from?"
print "[dfw, hkg, iad, ord, syd]"
dc_choice = raw_input().lower()

#if initial input is valid, this will bypass the while loop
if dc_choice == 'dfw' or dc_choice == 'hkg' or dc_choice == 'iad' or\
   dc_choice == 'ord' or dc_choice == 'syd':
    control = False
else:
    control = True

#if initial input is invalid, this will loop until it IS valid
while control:
    print "That's not a valid answer, please try again."

    print "Which DC do you want servers from?"
    print "[dfw, hkg, iad, ord, syd]"
    dc_choice = raw_input().lower()

    if dc_choice == 'dfw' or dc_choice == 'hkg' or dc_choice == 'iad' or\
       dc_choice == 'ord' or dc_choice == 'syd':
        control = False
    else:
        control = True

server_json = serverlist(dc_url.get(dc_choice) + '/servers', auth_header)

#Creating table with PrettyTable package
table = prettytable.PrettyTable(["Server Name", "UUID"])
table.align["Server Name"] = 'l' 
table.padding_width = 2

print "Your server names and UUID's are as follows: "

for i in server_json.get("servers"):
    table.add_row([i.get('name'), i.get('id')])

print table

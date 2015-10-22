# coding=utf-8
# Script to upload files to Parse

# Import correct libraries
import sys
import json,httplib,urllib

print str(sys.argv[1])
print str(sys.argv[2])

# Upload pics
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/files/pic'+sys.argv[1], open(sys.argv[2], 'rb').read(), {
       "X-Parse-Application-Id": "Application-Id",
       "X-Parse-REST-API-Key": "ASSBAmUvAChjkerTtrv0lbjynO0Uo7zCkk7LrmiB",
       "Content-Type": "image/jpeg"
     })
result = json.loads(connection.getresponse().read())
print result
name = result['name']

connection = httplib.HTTPSConnection('api.parse.com', 443)
params = urllib.urlencode({"where":json.dumps({
       "ID": int(sys.argv[1])
     })})
connection.connect()
connection.request('GET', '/1/classes/Clothes?%s' % params, '', {
       "X-Parse-Application-Id": "Application-Id",
       "X-Parse-REST-API-Key": "ASSBAmUvAChjkerTtrv0lbjynO0Uo7zCkk7LrmiB"
     })
result = json.loads(connection.getresponse().read())

if len(result['results']) == 1:
	objectId = result['results'][0]['objectId']
	print "objectId: " + objectId
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('PUT', '/1/classes/Clothes/'+objectId, json.dumps({
       "ID": int(sys.argv[1]),
       "Picture": {
         "name": name,
         "__type": "File"
       },
     }), {
       "X-Parse-Application-Id": "Application-Id",
       "X-Parse-REST-API-Key": "ASSBAmUvAChjkerTtrv0lbjynO0Uo7zCkk7LrmiB",
       "Content-Type": "application/json"
     })
	result = json.loads(connection.getresponse().read())
else:
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/classes/Clothes', json.dumps({
	       "ID": int(sys.argv[1]),
	       "Picture": {
	         "name": name,
	         "__type": "File"
	       }
	     }), {
	       "X-Parse-Application-Id": "Application-Id",
	       "X-Parse-REST-API-Key": "ASSBAmUvAChjkerTtrv0lbjynO0Uo7zCkk7LrmiB",
	       "Content-Type": "application/json"
	     })
	result = json.loads(connection.getresponse().read())

print result
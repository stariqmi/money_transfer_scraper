__author__ = 'salmantariqmirza'
import requests, json

API_KEY = "4ce9468052064a98867f3b550e3a12a9"
latest_url = "http://openexchangerates.org/api/latest.json?app_id={0}".format(API_KEY)

print latest_url

req = requests.get(latest_url)
json_obj =  json.loads(req.text)
print json_obj
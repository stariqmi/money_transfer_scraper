__author__ = 'salmantariqmirza'

import requests, json, datetime, time

API_KEY = "4ce9468052064a98867f3b550e3a12a9"
base_url = "http://openexchangerates.org/api/historical/"

d1 = datetime.date(2010,1,1)
d2 = datetime.date.today()

delta = d2 - d1

for i in range(delta.days + 1):
    hist_date = str(d1 + datetime.timedelta(days=i))
    hist_url = "{0}{1}.json?app_id={2}".format(base_url, hist_date, API_KEY)
    print hist_url
    req = requests.get(hist_url)
    json_obj = json.loads(req.text)
    print json_obj
    time.sleep(2)


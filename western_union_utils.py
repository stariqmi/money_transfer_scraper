__author__ = 'salmantariqmirza'

import urllib, urllib2, json, time

# Function to extract the exchange rate for a country
# @params country, a string representing the target country
def get_exchange_rate(country):
     # Create get request for exchange rate as json
    action = 'https://www.westernunion.com/ajaxHandler/service/getDelvryOptAndCurrency/?'
    query = {}
    query["originAmount"] = "1.0"
    query["originCountry"] = "US"
    query["targetCountry"] = country    # Request for specific country
    query["originCurrency"] = "USD"
    query["senderZipCode"] = "91025"
    data = urllib.urlencode(query)  # Encode for urls
    req = urllib2.Request(action + data)  # Create request object with action and query params
    req.add_header("Referer", "http://www.westernunion.com/Home")
    req.add_header("User-agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36")

    response = urllib2.urlopen(req)  # Perform request
    json_result = json.loads(response.read())  # Load json result into an object
    rate = json_result["update"]["conversion"]["targetAmount"]
    return rate

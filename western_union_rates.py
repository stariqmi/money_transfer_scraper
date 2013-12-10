#!/usr/bin/python

__author__ = 'salmantariqmirza'
import urllib, urllib2, json, time
from western_union_utils import get_exchange_rate

countries = ["TH","CN","PK","NG","IN","PH","ID","MX","GH","SO","ET"]

csv = open("western_rates.csv","w")
for country in countries:
    rate_str = get_exchange_rate(country)
    print(rate_str)
    csv.write(rate_str + "\n")
    time.sleep(5)
csv.close()
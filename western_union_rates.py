#!/usr/bin/python

__author__ = 'salmantariqmirza'
import time
from western_union_utils import get_exchange_rate

countries = ["TH","CN","PK","NG","IN","PH","ID","MX","GH","SO","ET"]

csv = open("mt_rails_app/lib/assets/rates/western_union_rates.csv","w")
for country in countries:
    print "Country Code: {0}".format(country)
    rate = get_exchange_rate(country)
    rate_str = "{0},{1}".format(country, rate)
    print(rate_str)
    csv.write(rate_str + "\n")
csv.close()
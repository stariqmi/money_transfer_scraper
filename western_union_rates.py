#!/usr/bin/python

__author__ = 'salmantariqmirza'
import time
from western_union_utils import get_exchange_rate

countries = ["TH","CN","PK","NG","IN","PH","ID","MX","GH","SO","ET"]
current_date = time.strftime("%d/%m/%Y")
current_time = time.strftime("%H:%M:%S")
today = "{0} {1}".format(current_date,current_time)

csv = open("western_rates.csv","w")
for country in countries:
    rate = get_exchange_rate(country)
    rate_str = "{0},{1},{2}".format(today, country, rate)
    print(rate_str)
    csv.write(rate_str + "\n")
csv.close()
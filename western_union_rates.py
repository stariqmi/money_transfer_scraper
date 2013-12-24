#!/usr/bin/python

__author__ = 'salmantariqmirza'

# Importing all required modules
import time
from western_union_utils import get_exchange_rate

# All country abbreviations
countries = ["TH","CN","PK","NG","IN","PH","ID","MX","GH","SO","ET"]

# Open relevant CSV file in rails application to write results of scraping to
csv = open("mt_rails_app/lib/assets/rates/western_union_rates.csv","w")
# Loop through all countries
for country in countries:
    # Format information from result
    print "Country Code: {0}".format(country)
    # Using util function
    rate = get_exchange_rate(country)
    rate_str = "{0},{1}".format(country, rate)
    print(rate_str)
    # Write to file
    csv.write(rate_str + "\n")

csv.close()
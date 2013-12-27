#!/usr/bin/python
__author__ = 'salmantariqmirza'

import xoom_utils as Utils

countries = [["IN", "INR"], ["PH", "PHP"], ["MX", "MXN"]]
amounts = ["100.00", "200.00", "300.00", "400.00", "500.00"]

# CSV file to write scraped rates
csv = open("../mt_rails_app/lib/assets/rates/xoom_fees.csv", "w")

# For country in countries
for country in countries:
    print "Country: {0}".format(country[0])
    
    # For each amount in amounts
    for amount in amounts:

    	# Scrape the fees and write them to the csv file
        print "Amount: {0}".format(amount)
        fees = Utils.get_fees(country[0], country[1], amount)
        print fees
        for fee in fees:
        	csv.write("{0},{1},{2},{3}\n".format(country[0], amount, fee[0], fee[1]))

csv.close()

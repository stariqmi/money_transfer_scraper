#!/usr/bin/python

__author__ = 'salmantariqmirza'

# Importing required modules
import requests
from selenium import webdriver
import lxml.html, time
from western_union_utils import get_exchange_rate, get_services_fees

# Using Selenium and PhantomJS to get all cookies
driver = webdriver.PhantomJS()
driver.get("http://www.westernunion.com/Home")
cookies = driver.get_cookies()
print cookies
driver.close()

# Create a cookies dictionary from cookies extracted by Selenium
cookie_dict = {}
for cookie in cookies:
    cookie_dict[cookie["name"]] = cookie["value"]

# All countries with abbreviations and currency codes
countries = [["PK", "PKR"],
            ["IN", "INR"],
            ["TH", "THB"],
            ["CN", "CNY"],
            ["NG", "NGN"],
            ["PH", "PHP"],
            ["ID", "IDR"],
            ["MX", "MXN"],
            ["GH", "GHS"],
            ["SO", "USD"],
            ["ET", "ETB"]
    ]

# All send amounts
send_amounts = ["100", "200", "300", "400", "500"]

# Open relevant CSV file in rails application to write results to
payment_options_file = open("mt_rails_app/lib/assets/rates/western_union_fees.csv","w")

# Looop through all the countries
for country in countries:
    # Loop through all the send amounts
    for send_amount in send_amounts:
        # Format information from results
        print "Country: {0}, Amount: {1}".format(country[0], send_amount)
        # Using the utils function
        payment_options = get_services_fees(country, cookie_dict, send_amount)
        # For each payment option from the results
        for option in payment_options:
            payment_str = "{0},{1},{2},{3},{4}".format(country[0], option["method"], option["time"], option["amount"], option["fee"])
            # Writing to CSV file
            payment_options_file.write(payment_str + "\n")
        print "sleeping for 5 seconds ... "
        time.sleep(5)

payment_options_file.close()
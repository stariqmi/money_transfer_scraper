#!/usr/bin/python

__author__ = 'salmantariqmirza'
import requests
from selenium import webdriver
import lxml.html, time
from western_union_utils import get_exchange_rate, get_services_fees

driver = webdriver.PhantomJS()
driver.get("http://www.westernunion.com/Home")
cookies = driver.get_cookies()
driver.close()

cookie_dict = {}
for cookie in cookies:
    cookie_dict[cookie["name"]] = cookie["value"]

countries = [["PK", "PKR"],
            ["IN", "INR"],
            ["TZ", "THB"],
            ["CN", "CNY"],
            ["NG", "NGN"],
            ["PH", "PHP"],
            ["ID", "IDR"],
            ["MX", "MXN"],
            ["GH", "GHS"],
            ["SO", "USD"],
            ["ET", "ETB"]
    ]

payment_options_file = open("mt_rails_app/lib/assets/rates/western_union_fees.csv","w")
for country in countries:

    payment_options = get_services_fees(country, cookie_dict)

    for option in payment_options:
        payment_str = "{0},{1},{2},{3},{4}".format(country[0], option["method"], option["time"], option["amount"], option["fee"])
        payment_options_file.write(payment_str + "\n")

payment_options_file.close()

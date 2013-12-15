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

current_date = time.strftime("%d/%m/%Y")
current_time = time.strftime("%H:%M:%S")
today = "{0} {1}".format(current_date,current_time)

payment_options_file = open("western_fees.csv","w")
for country in countries:

    payment_options = get_services_fees(country, cookie_dict)

    for option in payment_options:
        payment_str = "{0},{1},{2},{3},{4},{5}".format(today, country[0], option["method"], option["time"], option["amount"], option["fee"])
        payment_options_file.write(payment_str + "\n")

payment_options_file.close()

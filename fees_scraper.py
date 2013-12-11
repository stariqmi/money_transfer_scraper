#!/usr/bin/python

__author__ = 'salmantariqmirza'
import requests
from selenium import webdriver
import lxml.html
from western_union_utils import get_exchange_rate, get_services_fees

driver = webdriver.PhantomJS()
driver.get("http://www.westernunion.com/Home")
cookies = driver.get_cookies()
driver.close()

cookie_dict = {}
for cookie in cookies:
    cookie_dict[cookie["name"]] = cookie["value"]

countries = [["PK","PKR"], ["IN","INR"]]
for country in countries:
    get_services_fees(country, cookie_dict)
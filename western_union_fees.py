#!/usr/bin/python
__author__ = 'salmantariqmirza'

from selenium import webdriver
import time, urllib2, urllib, json
from western_union_utils import get_exchange_rate
import lxml.html

driver = webdriver.PhantomJS()
driver.get('http://www.westernunion.com/Home')
driver.find_element_by_link_text("Estimate price").click()
time.sleep(5)
driver.find_element_by_link_text("Estimate price").click()

# Extract REF_ID for post request
ref_id = driver.current_url.split("REF_ID=")[1][0:-2]
print ref_id

# Extract exchange rate for post request
rate = get_exchange_rate("PK")


# Extract all cookies for post request header
cookies = driver.get_cookies()
cookie_str = ""
for cookie in cookies:
    cookie_str += "{0}={1}; ".format(cookie["name"], cookie["value"])
cookie_str = cookie_str[0:-2]

# Create url encoded param string for post request
params = {}
params["body_tag:destination_country_iso_code"] = "PK"
params["body_tag:delivery_options"] = "000"
params["body_tag:price_estimate_zip:postal_code"] = "91025"
params["body_tag:principal_amount"] = "200"
params["body_tag:conversion_principal_amount"] = rate
params["body_tag:conversion_principal_amount_currency"] = "PKR"
params["body_tag:estimate_price_send_money"] = "Get Started"
params["REF_ID"] = ref_id
params["analyticsevents"] = ""
params["form_tracker"] = "destination_country_iso_code,delivery_options,postal_code,principal_amount,conversion_principal_amount,conversion_principal_amount_currency,estimate_price_send_money"
data = urllib.urlencode(params)  # Encode for urls

req = urllib2.Request("https://www.westernunion.com/price-estimator/continue", data) # Create request object with action and query params

# Add headers to request object
req.add_header("Cookie", cookie_str)
req.add_header("Referer", driver.current_url)
req.add_header("User-agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
(KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36")

response = urllib2.urlopen(req)  # Perform request

# Store response in an html file
post_html = open("post.html","w")
post_html.write(response.read())
post_html.close()

driver.close()

# lxml tree to parse html
elem_tree = lxml.html.parse("post.html")
fee_list = elem_tree.xpath('//*[@id="services_list_online"]')
print fee_list[0].find_class("row")[0].find_class("fee")[0].text_content().strip().replace("Fee","").strip()
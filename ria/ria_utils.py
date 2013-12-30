__author__ = 'salmantariqmirza'

import requests
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("https://www.riamoneytransfer.com/Pricing/PriceCalculator.aspx")
cookies = driver.get_cookies()

cookie_dict = {}
for cookie in cookies:
    cookie_dict[cookie["name"]] = cookie["value"]

headers = {
    "User-agent": 'Mozilla/5.0'
}

post_url = "https://www.riamoneytransfer.com/Pricing/PriceCalculator.aspx"

query = {
    "ctl00$ContentPlaceHolder1$ddCountryTo": "IN",
    "ctl00$ContentPlaceHolder1$countryHiddenField": "IN",
    "ctl00$ContentPlaceHolder1$txtAmount": 100,
    "ctl00$ContentPlaceHolder1$amountHiddenField": 100,
    "ctl00$ContentPlaceHolder1$ddCurrency": "INR",
    "ctl00$ContentPlaceHolder1$currencyHiddenField": "INR",
    "ctl00$ContentPlaceHolder1$btnEstimate": "Estimate Price",
    "ctl00$ContentPlaceHolder1$IsPostback": 0
}

#req = requests.post(post_url, params=query, cookies=cookie_dict, headers=headers)
req_2 = requests.get("https://www.riamoneytransfer.com/Pricing/PriceCalculator.aspx", headers=headers)
ria_page = open("ria.html", "w")
ria_page.write(req_2.text.encode("utf-8"))
ria_page.close()
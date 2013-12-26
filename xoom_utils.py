__author__ = 'I840192'

import requests, lxml.html

#--------------------------------------------------------
# Extracts the exchange rate
# @params country, a string representing a country code
# @params currency, a string representing a currency code
#--------------------------------------------------------


def get_rates(country, currency):

    query = {
        "receiveCountryCode": country,
        "receiveCurrencyCode": currency,
        "sendAmount": "100.00",
        "disbursementType": "DEPOSIT"
    }

    req = requests.post("http://www.xoom.com/ajax/send/getstarted/amount", params=query)
    amt_file = open("amount.html", "w")
    amt_file.write(req.text)
    amt_file.close()

    amt_file = open("amount.html", "r")
    html = lxml.html.parse(amt_file)
    raw_rate = html.xpath('//span[@id="exchangeRate"]')[0].text_content()
    rate = raw_rate.split("=")[1].strip().split()[0]
    amt_file.close()

    return rate


#--------------------------------------------------------
# Extracts the fees
# @params country, a string representing a country code
# @params currency, a string representing a currency code
# @params amount, a string representing the amount sent
#--------------------------------------------------------


def get_fees(country, currency, amount):
    query = {
        "receiveCountryCode": country,
        "receiveCurrencyCode": currency,
        "recipientId": "0",
        "sendAmount": amount,
        "accountType": "CHECKING",
        "paymentType": "ACH"
    }

    req2 = requests.post("https://www.xoom.com/ajax/send/getstarted/payout/deposit", params=query)
    pay_file = open("payment.html", "w")
    pay_file.write(req2.text)
    pay_file.close()

    pay_file = open("payment.html","r")
    html = lxml.html.parse(pay_file)

    fees = []

    methods_html = html.xpath('//input[@name="accountType"]')
    for method in methods_html:
        fees.append([method.attrib["value"]])

    counter = 0
    fees_html = html.xpath('//span[@class="fee payment-fee"]')
    for fee in fees_html:
        fees[counter].append(fee.text_content().strip())
        counter += 1

    pay_file.close()
    return fees

print get_rates("IN", "INR")
print get_fees("IN", "INR", "100.00")

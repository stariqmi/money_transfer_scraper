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

    # Save response to file
    amt_file = open("amount.html", "w")
    amt_file.write(req.text)
    amt_file.close()

    # Parse saved response
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

    req = ""

    # If country is India
    if country == "IN":
        query = {
            "receiveCountryCode": country,
            "receiveCurrencyCode": currency,
            "recipientId": "0",
            "sendAmount": amount,
            "accountType": "CHECKING",
            "paymentType": "ACH"
        }
        req = requests.post("https://www.xoom.com/ajax/send/getstarted/payout/deposit", params=query)

    # If country is Philippines, Mexico
    else:
        query = {
            "receiveCountryCode": country,
            "receiveCurrencyCode": currency,
            "recipientId": "0",
            "sendAmount": amount,
            "disbursementType": "PICKUP"
        }
        req = requests.post("https://www.xoom.com/ajax/send/getstarted/payout", params=query)

    # Save response to file for parsing
    pay_file = open("payment.html", "w")
    pay_file.write(req.text)
    pay_file.close()

    # Parse saved file
    pay_file = open("payment.html","r")
    html = lxml.html.parse(pay_file)

    fees = []

    # Get payment types
    methods_html = html.xpath('//input[@name="accountType"]')
    for method in methods_html:
        fees.append([method.attrib["value"]])

    # Get payment type fees
    counter = 0
    fees_html = html.xpath('//span[@class="fee payment-fee"]')
    for fee in fees_html:
        fees[counter].append(fee.text_content().strip())
        counter += 1

    pay_file.close()
    return fees

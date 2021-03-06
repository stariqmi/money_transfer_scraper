__author__ = 'salmantariqmirza'

import json, requests, lxml.html


# Function to extract the exchange rate for a country
# @params country, a string representing the target country


def get_exchange_rate(country):
     # Create get request for exchange rate as json
    action = 'https://www.westernunion.com/ajaxHandler/service/getDelvryOptAndCurrency/?'
    query = {}
    query["originAmount"] = "1.0"
    query["originCountry"] = "US"
    query["targetCountry"] = country    # Request for specific country
    query["originCurrency"] = "USD"
    query["senderZipCode"] = "91025"
    req = requests.get(action, params=query)
    json_result = json.loads(req.text)  # Load json result into an object
    rate = json_result["update"]["conversion"]["targetAmount"]
    return rate

# Function to extract the fees for sending an amount
# @params country, a string representing a target country
# @params cookie_dict, a dictionary of cookies
# @params send_amount, integer representing the send amount

def get_services_fees(country, cookie_dict, send_amount):
    # Create a get request to get REF_ID needed for main post request
    req = requests.get('http://www.westernunion.com/WUCOMWEB/shoppingAreaAction.do?method=load&nextSecurePage=Y', cookies=cookie_dict)
    
    # Save the response html in a html file
    ep_html = open("estimate_price.html", "w")
    ep_html.write(req.text.encode("utf-8"))
    ep_html.close()

    # Parsing through the response html
    ep_lxml = lxml.html.parse("estimate_price.html")
    meta_tags = ep_lxml.xpath("//meta")
    ref_id = ""
    # Looping through all meta tags to find REF_ID
    for tag in meta_tags:
        content = tag.get("content")
        if not content == None:
            if content.find("REF_ID=") != -1:
                ref_id = content.split("REF_ID=")[1]

    # Get exchange rate needed for post request
    rate = get_exchange_rate(country[0])

    # Setting up the params for post request
    params = {}
    params["body_tag:destination_country_iso_code"] = country[0]
    params["body_tag:delivery_options"] = "000"
    params["body_tag:price_estimate_zip:postal_code"] = "91025"
    params["body_tag:principal_amount"] = send_amount
    params["body_tag:conversion_principal_amount"] = rate
    params["body_tag:conversion_principal_amount_currency"] = country[1]
    params["body_tag:estimate_price_send_money"] = "Get Started"
    params["REF_ID"] = ref_id
    params["analyticsevents"] = ""
    params["form_tracker"] = "destination_country_iso_code,delivery_options,postal_code,principal_amount,conversion_principal_amount,conversion_principal_amount_currency,estimate_price_send_money"

    # Performing the post request
    post_req = requests.post("https://www.westernunion.com/price-estimator/continue", params=params, cookies=cookie_dict)
    
    # Saving the html response of the post request in html file
    fees_html = open("fees_page.html","w")
    fees_html.write(post_req.text.encode("utf-8"))
    fees_html.close()

    # Parsing through the response html
    fees_lxml = lxml.html.parse("fees_page.html")
    # Search for all services
    service_list = fees_lxml.xpath('//ul[@id="tab_send_online_ul"]/li[@class="option"]/div[@class="row clearfix"]')
    payment_methods = []

    # Loop through all found services
    for service in service_list:
        #Extract the relevant data from each service to create a payment dictionary
        payment = {}
        payment["method"] = service.xpath('./div[@class="twocol"]/p')[0].text
        payment["time"] = service.xpath('./div[@class="available"]/div/p')[0].text
        payment["amount"] = service.xpath('./div[@class="amount"]/p/span')[0].text + " " + service.xpath('./div[@class="amount"]/p/span')[1].text
        payment["fee"] = service.xpath('./div[@class="fee"]/p/span')[0].text + " " + service.xpath('./div[@class="fee"]/p/span')[1].text
        print payment
        # Add payment dictionary to array
        payment_methods.append(payment)
        
    return payment_methods
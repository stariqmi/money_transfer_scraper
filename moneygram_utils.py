from selenium import webdriver
import requests, lxml.html

def get_cookies():
    cookies = {}
    driver = webdriver.PhantomJS() # Driver to extract cookies
    driver.get("https://www.moneygram.com/wps/portal/moneygramonline/home/sendmoney/!ut/p/c5/04_SB8K8xLLM9MSSzPy8xBz9CP0os3gPSxcDDxN_A0t_Q18DA08LUy8_M3NDQwN3I_1wkA4kFe5h7i5AFRbGxk7ersYGFgYQeQMcwNFA388jPzdVvyA7O83RUVERAJo0HXM!/dl3/d3/L2dBISEvZ0FBIS9nQSEh/?CC=US&LC=en-US#")

    # Extract all cookies in 
    for cookie in driver.get_cookies():
        cookies[cookie["name"]] = cookie["value"]
    driver.close()
    return cookies


def get_rate(cookies, country, amount=1):
    # Construct query params 
    query = {}
    query["fCountry"] = "USA"
    query["dCountry"] = country[1]

    # Post request to get param for main post request
    req = requests.post("https://www.moneygram.com/wps/mgo/jsps/estimator/estimatorServiceAtLocation.jsp", params=query, cookies=cookies)

    # Save response as html for parsing
    req.encoding = "utf-8"
   
    # Append new cookies to cookie dictionary 
    for cookie in req.cookies:
        cookies[cookie.name] = cookie.value

    response_file = open("location.html", "w")
    response_file.write(req.text)
    response_file.close()
    response_file = open("location.html")
    html = lxml.html.parse(response_file)

    # Extract service value from response html
    service = html.xpath("//option")[1].attrib["value"]

    # Construct main query 
    main_query = {}
    main_query["fCountry"] = "USA"
    main_query["dCountry"] = country[1]
    main_query["sService"] = service
    main_query["transferMode"] = "online"
    main_query["samount"] = amount
    main_query["rewardsID"] = ""

    # Post request to get html response that has exchange rate and fees
    post = requests.post("https://www.moneygram.com/wps/mgo/jsps/estimator/onlineEstimatorSubmit.jsp", params=main_query, cookies=cookies)
    
    # Manipulate json response
    json =  post.json()
    info = {"rate": json["exrate"], "economy": json["economy"], "sameday": json["sameday"], "country": country[0]}
    return info



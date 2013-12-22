from selenium import webdriver
import requests, lxml.html

def get_cookies():
    cookies = {}
    driver = webdriver.PhantomJS() # Driver to extract cookies
    driver.get("https://www.moneygram.com/wps/portal/moneygramonline/home/estimator?LC=en-US")

    # Extract all cookies in 
    for cookie in driver.get_cookies():
        cookies[cookie["name"]] = cookie["value"]
    driver.close()
    return cookies
    
def get_rate(cookies, country):
    # Construct query params 
    query = {}
    query["fCountry"] = "USA"
    query["dCountry"] = country[1]

    # Post request to get param for main post request
    req = requests.post("https://www.moneygram.com/wps/mgo/jsps/estimator/estimatorServiceAtLocation.jsp", params=query, cookies=cookies)

    # Save response as html for parsing
    req.encoding = "utf-8"
    response_file = open("location.html", "w")
    response_file.write(req.text)
    response_file.close()
    response_file = open("location.html")
    html = lxml.html.parse(response_file)

    # Extract service value from response html
    service = html.xpath("//option")[1].attrib["value"]

    # Construct remaining query 
    query["fCurrency"] = "USD"
    query["sService"] = service
    query["srOpt"] = "sendAmount"
    query["transferMode"] = "location"
    query["samount"] = 1
    query["receiveMoney"] = "false"
    query["isOnline"] = "no"
    query["rewardsID"] = ""

    # Post request to get html response that has exchange rate and fees
    post = requests.post("https://www.moneygram.com/wps/mgo/jsps/estimator/estimatorSubmit.jsp", params=query, cookies=cookies)
    
    # Save response html for parsing 
    post_html = open("post.html", "w")
    post_html.write(post.text)
    post_html.close()
    post_html = open("post.html")
    rates_html = lxml.html.parse(post_html)

    # Extract rate from response html 
    raw_rate = rates_html.xpath('//span[@class="exRate"]')[0].text_content()
    raw_fees = rates_html.xpath('//p[@class="redTitle"]')[0].text_content()
    rate = raw_rate.strip()
    fee = raw_fees.strip()
    print "{0} \t {1} \t {2}".format(country, rate, fee)
    return {"rate":rate, "fee":fee}


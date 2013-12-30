from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# PhantomJS
#d_cap = dict(DesiredCapabilities.PHANTOMJS)
#d_cap["phantomjs.page.settings.userAgent"] = (
#    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
#    "(KHTML, like Gecko) Chrome/15.0.87"
#)
#driver = webdriver.PhantomJS(desired_capabilities=d_cap)

# Firefox
driver = webdriver.Firefox()

driver.get("https://www.riamoneytransfer.com/Pricing/PriceCalculator.aspx")
ria = open("ria.html", "w")
ria.write(driver.page_source.encode("utf-8"))
ria.close()

inputs = driver.find_elements_by_tag_name("input")
for input_tag in inputs:
    print "{0} : {1}".format(input_tag.get_attribute("name"), input_tag.get_attribute("value"))

driver.close()

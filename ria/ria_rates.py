from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from ria_utils import get_rate

# Array to hold all country codes used in post request params
countries = [
             ["TH","Thailand"],
             ["CN","China"],
             ["PK","Pakistan"],
             ["IN","India"],
             ["PH","Philippines"],
             ["ID","Indonesia"],
             ["MX","Mexico"],
             ["GH","Ghana"],
             ["ET","Ethiopia"]
            ]

# PhantomJS
d_cap = dict(DesiredCapabilities.PHANTOMJS)
d_cap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)
driver = webdriver.PhantomJS(desired_capabilities=d_cap)

# Firefox
#driver = webdriver.Firefox()

driver.get("https://www.riamoneytransfer.com/Pricing/PriceCalculator.aspx")

for country in countries:
    rate = get_rate(driver, country)
    print "Exchange Rate for {0}: {1}".format(country[1], rate)
driver.close()
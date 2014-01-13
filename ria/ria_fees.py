from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from ria_utils import get_fee

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

# Amount
amounts = ["100", "200", "300", "400", "500"]

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
    print "Country: {0}".format(country[1])
    for amount in amounts:
        print "\t- Amount: {0}".format(amount)
        fees = get_fee(driver, country, amount)
        for fee in fees:
            print "\t\t- {0}: {1}".format(fee[0], fee[1])
driver.close()
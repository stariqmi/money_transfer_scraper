__author__ = 'salmantariqmirza'

import moneygram_utils

# Array to hold all country cdoes used in post request params
countries = ["THA", "CHN", "PAK", "NER", "IND", "PHL", "IDN", "MEX", "GHA", "ETH"]

print "\nCountry  Rate \t Fees"
print "-------------------------"

# Get cookies
cookies = moneygram_utils.get_cookies()

# For each country
for country in countries:
    moneygram_utils.get_rate(cookies, country)

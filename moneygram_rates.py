__author__ = 'salmantariqmirza'

import moneygram_utils

# Array to hold all country cdoes used in post request params
countries = [
             ["TH","THA"], 
             ["CN","CHN"], 
             ["PK","PAK"], 
             ["NG","NER"], 
             ["IN","IND"], 
             ["PH","PHL"], 
             ["ID","IDN"], 
             ["MX","MEX"], 
             ["GH","GHA"], 
             ["ET","ETH"]
            ]

print "\nCountry  Rate"
print "---------------------"

# Get cookies
cookies = moneygram_utils.get_cookies()

# Open file to write results to
rates_file = open("mt_rails_app/lib/assets/rates/moneygram_rates.csv", "w")
 
# For each country
for country in countries:
    result = moneygram_utils.get_rate(cookies, country)
    print "{0} \t {1}".format(result["country"], result["rate"])
    rates_file.write("{0},{1}\n".format(result["country"], result["rate"]))

# Close result file
rates_file.close()

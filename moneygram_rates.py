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

print "\nCountry  Rate \t Fees"
print "-------------------------"

# Get cookies
cookies = moneygram_utils.get_cookies()

# Open files to write results to
rates_file = open("mt_rails_app/lib/assets/rates/moneygram_rates.csv", "w")
fees_file = open("mt_rails_app/lib/assets/rates/moneygram_fees.csv", "w")
 
# For each country
for country in countries:
    result = moneygram_utils.get_rate(cookies, country)
    rates_file.write("{0},{1}\n".format(country[0], result["rate"]))
    fees_file.write("{0},{1}\n".format(country[0], result["fee"]))

# Close result files
rates_file.close()
fees_file.close()

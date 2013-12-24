#!/usr/bin/python
import moneygram_utils as Utils

# Country codes 
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

# Send Amounts
send_amounts = [100, 200, 300, 400, 500]

# Get cookies 
cookies = Utils.get_cookies()

# Open file to write results to
fees_file = open("mt_rails_app/lib/assets/rates/moneygram_fees.csv", "w")

print "Country  Amount  Rate  Sameday  Economy"
print "----------------------------------------"

# For each country
for country in countries:
    for amount in send_amounts:
        result  = Utils.get_rate(cookies, country, amount=amount)
        fees_file.write("{0},{1},{2},{3},{4}\n".format(result["country"], amount, result["rate"], result["sameday"], result["economy"]))
        print "{0}  {1}  {2}  {3}  {4}".format(result["country"], amount, result["rate"], result["sameday"], result["economy"])

# Close result file
fees_file.close()

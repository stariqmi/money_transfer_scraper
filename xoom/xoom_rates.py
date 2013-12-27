__author__ = 'salmantariqmirza'

import xoom_utils as Utils

countries = [["IN", "INR"], ["PH", "PHP"], ["MX", "MXN"]]

# CSV file to write scraped rates
csv = open("../mt_rails_app/lib/assets/rates/xoom_rates.csv", "w")

# For each country in the list of countries
for country in countries:
	# Extract rate and wite to csv file
    rate = Utils.get_rates(country[0], country[1])
    csv.write("{0},{1}\n".format(country[0], rate))
    print "Country: {0}, Rate: {1}".format(country[0], rate)

csv.close()	# Close csv file
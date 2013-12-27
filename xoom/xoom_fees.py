__author__ = 'salmantariqmirza'

import xoom_utils as Utils

countries = [["IN", "INR"], ["PH", "PHP"], ["MX", "MXN"]]
amounts = ["100.00", "200.00", "300.00", "400.00", "500.00"]

for country in countries:
    for amount in amounts:
        print "Country: {0}, Amount: {1}".format(country[0], amount)
        fee = Utils.get_fees(country[0], country[1], amount)
        print fee
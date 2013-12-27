__author__ = 'salmantariqmirza'

import xoom_utils as Utils

countries = [["IN", "INR"], ["PH", "PHP"], ["MX", "MXN"]]

for country in countries:
    rate = Utils.get_rates(country[0], country[1])

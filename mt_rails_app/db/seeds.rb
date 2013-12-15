# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
destinations = [["TH", "Thailand"],
				["CN", "China"],
				["PK", "Pakistan"],
				["NG", "Nigeria"],
				["IN", "India"],
				["PH", "Philippines"],
				["ID", "Indonesia"],
				["MX", "Mexico"],
				["GH", "Ghana"],
				["SO", "Somalia"],
				["ET", "Ethiopia"]
	]
destinations.each do |dest|
	DestinationCountry.create({abbreviation: dest[0], name: dest[1]})
end

operators = [["Western Union", "http://www.westernunion.com/Home"]]
operators.each do |op|
	Operator.create({name: op[0], website: op[1]})
end

payment_methods = ["Bank Tarnsfer through WU", "Credit/Debit", "Bank Transfer"]
payment_methods.each do |method|
	PaymentMethod.create({method: method})
end

receive_methods = ["Cash at Agent Location"]
receive_methods.each do |method|
	ReceiveMethod.create({method: method})
end

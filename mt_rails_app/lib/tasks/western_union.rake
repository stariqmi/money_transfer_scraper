namespace :western_union do
  desc "Parse Western Union Fees"
  task fees: :environment do
  end

  desc "Parse Western Union Rates"
  task rates: :environment do
  	operator = Operator.where(name: "Western Union")
  	# puts operator[0].id
  	File.open("#{Rails.root}/lib/assets/rates/western_union_rates.csv").each do |line|
  		data = line.split(",")
  		destination = DestinationCountry.where(abbreviation: data[0])
  		# puts destination[0].inspect
  		rate = FxRate.create({rate: data[1].to_f, timestamp: DateTime.now, operator_id: operator[0].id,
                             destination_country_id: destination[0].id, receive_method_id: 1})
  		puts rate.inspect
  	end
  end

  desc "Destroy all Western Union Rates records"
  task destroy: :environment do
  	FxRate.all.each do |rate|
  		if rate.operator.name == "Western Union"
  			rate.delete
  		end
  	end
  end

end

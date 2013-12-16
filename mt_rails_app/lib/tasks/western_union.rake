namespace :western_union do
  desc "Parse Western Union Fees"
  task fees: :environment do
    operators = Operator.where(name: "Western Union")
    File.open("#{Rails.root}/lib/assets/rates/western_union_fees.csv").each do |line|
      data = line.split(",")
      destinations = DestinationCountry.where(abbreviation: data[0])
      payment_methods = PaymentMethod.where(method: data[1])
      send_amounts = SendAmount.where(amount: data[3].split(" ")[0].to_f)
      parsed_fee = data[-1].split(" ")[0].to_f
      fee = FxFee.create({fee: parsed_fee, timestamp: DateTime.now, operator_id: operators[0].id, 
                          destination_country_id: destinations[0].id, receive_method_id: 1,
                          send_amount_id: send_amounts[0].id, payment_method_id: payment_methods[0].id,
                          time_estimate: data[2]})
      puts fee.inspect
    end
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
  task destroy_rates: :environment do
  	FxRate.all.each do |rate|
  		if rate.operator.name == "Western Union"
  			rate.delete
  		end
  	end
  end

  desc "Destroy all Western Union Fees records"
  task destroy_fees: :environment do
    FxFee.all.each do |fee|
      if fee.operator.name == "Western Union"
        fee.delete
      end
    end
  end

end

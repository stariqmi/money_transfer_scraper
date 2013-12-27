namespace :xoom do
    desc "Parse Xoom Fees"
    task fees: :environment do
        operators = Operator.where(name: "Xoom")
        File.open("#{Rails.root}/lib/assets/rates/xoom_fees.csv").each do |line|
            data = line.split(",")
            country = data[0]
            destinations = DestinationCountry.where(abbreviation: data[0])
            send_amounts = SendAmount.where(amount: data[1].to_f)
            payment_options = PaymentMethod.where(method: "Xoom " << data[2])
            fees_raw = data[3].to_f
            fees = FxFee.create({fee: fees_raw, timestamp: DateTime.now, operator_id: operators[0].id, destination_country_id: destinations[0].id, receive_method_id: 1, 
                                    send_amount_id: send_amounts[0].id, payment_method_id: payment_methods[0].id, time_estimate: "Unknown"})  
            puts fees.inspect
        end
    end

    desc "Parse Xoom Rates"
    task rates: :environment do
        operators = Operator.where(name: "Xoom")
        File.open("#{Rails.root}/lib/assets/rates/xoom_rates.csv").each do |line|
            data = line.split(",")
            country = data[0]
            rate_text = data[1]
            destinations = DestinationCountry.where(abbreviation: country)
            rate = FxRate.create({rate: rate_text.to_f, timestamp: DateTime.now, operator_id: operators[0].id, destination_country_id: destinations[0].id, receive_method_id: 1})
            puts rate.inspect
        end
    end
end
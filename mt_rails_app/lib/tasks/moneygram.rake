namespace :moneygram do
    desc "Parse MoneyGram Fees"
    task fees: :environment do
        operators = Operator.where(name: "MoneyGram")
        File.open("#{Rails.root}/lib/assets/rates/moneygram_fees.csv").each do |line|
            data = line.split(",")
            country = data[0]
            destinations = DestinationCountry.where(abbreviation: data[0])
            send_amounts = SendAmount.where(amount: data[1].to_f)
            payment_online_economy = PaymentMethod.where(method: "MoneyGram Online Economy")
            payment_online_sameday = PaymentMethod.where(method: "MoneyGram Online Sameday")
            sameday_fee = data[3].to_f
            economy_fee = data[4].to_f 
            puts payment_online_sameday[0].id
            economy_fee = FxFee.create({fee: economy_fee, timestamp: DateTime.now, operator_id: operators[0].id, destination_country_id: destinations[0].id, receive_method_id: 1, send_amount_id: send_amounts[0].id, payment_method_id: payment_online_economy[0].id, time_estimate: "3 Days"})  
            sameday_fee = FxFee.create({fee: sameday_fee, timestamp: DateTime.now, operator_id: operators[0].id, destination_country_id: destinations[0].id, receive_method_id: 1, send_amount_id: send_amounts[0].id, payment_method_id: payment_online_sameday[0].id, time_estimate: "In 10 minutes"})  
            puts economy_fee.inspect
            puts sameday_fee.inspect
        end
    end

    desc "Parse MoneyGram Rates"
    task rates: :environment do
        operators = Operator.where(name: "MoneyGram")
        File.open("#{Rails.root}/lib/assets/rates/moneygram_rates.csv").each do |line|
            data = line.split(",")
            country = data[0]
            rate_text = data[1]
            destinations = DestinationCountry.where(abbreviation: country)
            rate = FxRate.create({rate: rate_text.to_f, timestamp: DateTime.now, operator_id: operators[0].id, destination_country_id: destinations[0].id, receive_method_id: 1})
            puts rate.inspect
        end
    end
end

namespace :moneygram do
    desc "Parse MoneyGram Fees"
    task fees: :environment do
        operators = Operator.where(name: "MoneyGram")
        File.open("#{Rails.root}/lib/assets/rates/moneygram_fees.csv").each do |line|
            data = line.split(",")
            country = data[0]
            fee_text = data[1].split()[0]
        end
    end

    desc "Parse MoneyGram Rates"
    task rates: :environment do
        operators = Operator.where(name: "MoneyGram")
        File.open("#{Rails.root}/lib/assets/rates/moneygram_rates.csv").each do |line|
            data = line.split(",")
            country = data[0]
            rate_text = data[1].split()[0]
            destinations = DestinationCountry.where(abbreviation: country)
            rate = FxRate.create({rate: rate_text.to_f, timestamp: DateTime.now, operator_id: operators[0].id, destination_country_id: destinations[0].id, receive_method_id: 1})
            puts rate.inspect
        end
    end
end

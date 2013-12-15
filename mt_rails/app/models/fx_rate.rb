class FxRate < ActiveRecord::Base
	has_one :destination_country
	has_one :operator
	has_one :payment_method
	has_one :send_amount
end

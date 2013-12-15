class PaymentMethod < ActiveRecord::Base
	belongs_to :fx_rate
end

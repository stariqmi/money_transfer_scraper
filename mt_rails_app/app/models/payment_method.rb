class PaymentMethod < ActiveRecord::Base
	validates :method, uniqueness: true
end

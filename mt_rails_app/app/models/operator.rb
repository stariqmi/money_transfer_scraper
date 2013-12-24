class Operator < ActiveRecord::Base
	validates :name, uniqueness: true
    has_many :fx_rates
    has_many :fx_fees
end

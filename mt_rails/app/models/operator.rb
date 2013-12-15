class Operator < ActiveRecord::Base
	validates :name, uniqueness: true
	belongs_to :fx_rate
end

class Operator < ActiveRecord::Base
	validates :name, uniqueness: true
end

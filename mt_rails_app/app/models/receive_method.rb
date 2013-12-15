class ReceiveMethod < ActiveRecord::Base
	validates :method, uniqueness: true
end

class DestinationCountry < ActiveRecord::Base
	validates :abbreviation, uniqueness: true
end

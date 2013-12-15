class FxRate < ActiveRecord::Base
  belongs_to :operator
  belongs_to :destination_country
  belongs_to :payment_method
  belongs_to :receive_method
end

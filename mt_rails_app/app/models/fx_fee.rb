class FxFee < ActiveRecord::Base
  belongs_to :send_amount
  belongs_to :operator
  belongs_to :destination_country
  belongs_to :payment_method
  belongs_to :receive_method
end

class AddTimeEstimateToFxFee < ActiveRecord::Migration
  def change
    add_column :fx_fees, :time_estimate, :string
  end
end

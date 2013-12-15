class CreateFxRates < ActiveRecord::Migration
  def change
    drop_table :fx_rates
    create_table :fx_rates do |t|
      t.references :operator, index: true
      t.references :destination_country, index: true
      t.references :payment_method, index: true
      t.references :receive_method, index: true
      t.decimal :rate
      t.datetime :timestamp

      t.timestamps
    end
  end
end

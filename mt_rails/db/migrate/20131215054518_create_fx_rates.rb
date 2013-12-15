class CreateFxRates < ActiveRecord::Migration
  def change
    create_table :fx_rates do |t|
      t.decimal :rate
      t.timestamp :timestamp

      t.timestamps
    end
  end
end

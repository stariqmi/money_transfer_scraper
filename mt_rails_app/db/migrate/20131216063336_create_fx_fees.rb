class CreateFxFees < ActiveRecord::Migration
  def change
    create_table :fx_fees do |t|
      t.references :send_amount, index: true
      t.references :operator, index: true
      t.references :destination_country, index: true
      t.references :payment_method, index: true
      t.references :receive_method, index: true
      t.decimal :fee
      t.datetime :timestamp

      t.timestamps
    end
  end
end

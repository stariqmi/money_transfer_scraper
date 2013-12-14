class CreateSendAmounts < ActiveRecord::Migration
  def change
    create_table :send_amounts do |t|
      t.decimal :amount

      t.timestamps
    end
  end
end

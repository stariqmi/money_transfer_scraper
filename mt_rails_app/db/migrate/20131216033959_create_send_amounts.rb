class CreateSendAmounts < ActiveRecord::Migration
  def change
    create_table :send_amounts do |t|
      t.integer :amount

      t.timestamps
    end
  end
end

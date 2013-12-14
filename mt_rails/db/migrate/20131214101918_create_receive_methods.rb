class CreateReceiveMethods < ActiveRecord::Migration
  def change
    create_table :receive_methods do |t|
      t.string :method

      t.timestamps
    end
  end
end

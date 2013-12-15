class CreateReveiveMethods < ActiveRecord::Migration
  def change
    create_table :reveive_methods do |t|
      t.string :method

      t.timestamps
    end
  end
end

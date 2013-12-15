class CreateDestinationCountries < ActiveRecord::Migration
  def change
    create_table :destination_countries do |t|
      t.string :name
      t.string :abbreviation

      t.timestamps
    end
  end
end

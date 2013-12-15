class AddAbbreviationToDestinationCountry < ActiveRecord::Migration
  def change
    add_column :destination_countries, :abbrevitaion, :string
  end
end

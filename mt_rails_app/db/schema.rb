# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20131215083658) do

  create_table "destination_countries", force: true do |t|
    t.string   "name"
    t.string   "abbreviation"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "fx_rates", force: true do |t|
    t.integer  "operator_id"
    t.integer  "destination_country_id"
    t.integer  "payment_method_id"
    t.integer  "receive_method_id"
    t.decimal  "rate"
    t.datetime "timestamp"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  add_index "fx_rates", ["destination_country_id"], name: "index_fx_rates_on_destination_country_id"
  add_index "fx_rates", ["operator_id"], name: "index_fx_rates_on_operator_id"
  add_index "fx_rates", ["payment_method_id"], name: "index_fx_rates_on_payment_method_id"
  add_index "fx_rates", ["receive_method_id"], name: "index_fx_rates_on_receive_method_id"

  create_table "operators", force: true do |t|
    t.string   "name"
    t.string   "website"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "payment_methods", force: true do |t|
    t.string   "method"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "receive_methods", force: true do |t|
    t.string   "method"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "reveive_methods", force: true do |t|
    t.string   "method"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

end

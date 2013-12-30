./western_union_rates.py
./western_union_fees.py
./moneygram_rates.py
./moneygram_fees.py

cd xoom

./xoom_rates.py
./xoom_fees.py

cd ../mt_rails_app

/home/ec2-user/.rvm/bin/rake western_union:rates
/home/ec2-user/.rvm/bin/rake western_union:fees
/home/ec2-user/.rvm/bin/rake moneygram:rates
/home/ec2-user/.rvm/bin/rake moneygram:fees
/home/ec2-user/.rvm/bin/rake xoom:rates
/home/ec2-user/.rvm/bin/rake xoom.fees

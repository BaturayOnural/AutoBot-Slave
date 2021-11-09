#!/usr/bin/env bash
rm chromedriver
apt install -y python3-virtualenv
virtualenv env
source ./env/bin/activate
pip install -r requirements.txt
apt update -y
apt upgrade -y
apt install -y libxss1 libappindicator1 libindicator7
apt install -y unzip
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
apt-get install -f -y
wget https://chromedriver.storage.googleapis.com/95.0.4638.69/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
python3 test_selenium.py

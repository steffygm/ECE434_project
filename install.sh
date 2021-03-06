#!/bin/bash

sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-imaging git
git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack.git
cd Adafruit_Python_LED_Backpack
sudo python setup.py install
git clone https://github.com/adafruit/Adafruit_Python_PureIO.git
cd Adafruit_Python_PureIO
sudo python setup.py install
git clone https://github.com/adafruit/adafruit-beaglebone-io-python.git
cd adafruit-beaglebone-io-python
sudo python setup.py install

echo "Installing jumbotron essentials"

sudo apt install fbset
sudo apt install fbi

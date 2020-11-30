echo 'This script must be run as root!.  Besure to run this as:  sudo ./setup.sh'

apt-get update
apt-get upgrade
apt-get install python3-pip
apt-get install -y python-smbus
apt-get install -y i2c-tools

pip3 install -r requirements.txt

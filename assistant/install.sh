dir=$(pwd)
cd $dir
# Make executables
chmod +x run.sh
chmod +x uninstall.sh
cd flask/
chmod +x run_dev.sh
cd eapi/
chmod +x runtest.py

# Get dependencies
sudo apt install -y python
sudo apt install -y python-pip python-dev build-essential
sudo pip install --upgrade pip
pip install flask

command=".$dir/run.sh"
# build cron job
crontab -l | { cat; echo "00 8 * * 1-5 $command"; } | crontab -

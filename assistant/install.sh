dir=$(pwd)
cd $dir
# Make executables
chmod +x run.sh
cd flask/
chmod +x run_dev.sh
cd eapi/
chmod +x runtest.py

# Get dependencies
sudo apt install -y python
sudo apt install -y python-pip python-dev build-essential
sudo pip install --upgrade pip
pip install flask

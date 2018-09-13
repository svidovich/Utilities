dir=$pwd
crontab -u $USER -l | grep -v ".$dir/run.sh" | crontab -u $USER -

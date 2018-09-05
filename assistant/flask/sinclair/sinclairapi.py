# This file serves as a list of functions that will be used alongside Sinclair to ensure that
# everything goes swimmingly
import datetime
import os

# We want to be able to tell if it is currently midnight or not
# Each day we will send out a new batch of messages at midnight
# This ( midnight detector )
# It ( Detects whether the current time is midnight locally )
# Takes
# N/A
# Returns
# True if it is midnight
# False otherwise
def midnight():
	hour = str(datetime.datetime.now().time().hour)
	minute = str(datetime.datetime.now().time().minute)
	print("{} {}".format(hour, minute))
	if hour == '23' and minute == '59':
		return True
	else:
		return False

# We want to be able to tell the system that we have sent an email batch.
def has_sent_email():
	os.environ['batchsent'] = '1'


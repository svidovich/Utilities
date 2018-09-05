# This file serves as a list of functions that will be used alongside Sinclair to ensure that
# everything goes swimmingly
import datetime


def midnight():
	hour = str(datetime.datetime.now().time().hour)
	minute = str(datetime.datetime.now().time().minute)
	print("{} {}".format(hour, minute))
	if hour == '23' and minute == '59':
		return True
	else:
		return False

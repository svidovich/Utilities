import sys
import smtplib
import json
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


#####################################################################################
# The following functions are to do with the connection with the server required to #
# send emails.									    #
#####################################################################################

# This ( initializer )
# Takes
# > account: filename of json file with schema
# >> { login:email, password:emailpassword }	
# Returns
# server: SMTP connection to mail server

def initialize_client(account):
	# Set up a server that we can use
	print("Getting SMTP from gmail port 587...")
	try:
		server = smtplib.SMTP('smtp.gmail.com',587)
	except Exception as e:
		print("Problem setting up SMTP: {} Exiting...".format(e))
	print("Getting account details...")
	try:
		with open(account, 'r') as file:
			details = json.load(file)
	except Exception as e:
		print("Problem getting account details: {} Exiting...".format(e))
		exit(1)
	# Let's begin talking with the server
	try:
		print("Attempting to start tls...")
		server.starttls()
		server.login(details["login"], details["password"])
	except Exception as e:
		print("Exception occured during client initialization: {} Exiting...".format(e))
		server.quit()
		exit(1)
	return server


# This ( connection closer )
# Takes
# > server: connection to email SMTP server returned by initializer

def close_connection(server):
	try:
		print("Closing server connection...")
		server.quit()
		print("Session closed successfully.")
	except Exception as e:
		print("Exception occured when closing connection to SMTP: {}".format(e))



#########################################################################################
# The following functions are to do with sending files to singular destinations.        #
#########################################################################################

# This ( message builder )
# Takes
# > account: filename of json file with schema
# >> { login:email, password:emailpassword }	
# > recipient: filename of json file with schema
# >> { destination:recipientemailaddress } 
# > emailmessage: filename of json file with schema
# >> { subject:emailsubjectline, body:emailbodytosend }
# Returns
# > email message according to python MIME lib as string

def construct_message(account, recipient, emailmessage):
	try:
		print("Getting details for construction of message...")
		with open(account, 'r') as file:
			details = json.load(file)
		with open(recipient, "r") as file:
			destination = json.load(file)
		with open(emailmessage, "r") as file:
			message = json.load(file)
		print("Details retrieved successfully.")
	except Exception as e:
		print("An Exception occured when constructing an email message: {} Exiting...".format(e))
		# We want to exit here because if we can't open these files and continue, we will be
		# constructing a bunch of null garbage.
		exit(1)
	msg = MIMEMultipart()
	msg['From'] = details["login"]
	msg['To'] = destination["destination"]
	msg['Subject'] = message["subject"]
	msg.attach(MIMEText(message["body"], 'plain'))
	msg = msg.as_string()
	return msg

# This ( message sender )
# Takes
# > account: filename of json file with schema
# >> { login:email, password:emailpassword }	
# > recipient: filename of json file with schema
# >> { destination:recipientemailaddress )
# > message: string constructed by python MIME library; returned by construct_message
# > server: connection to email SMTP server returned by initializer
# Returns
# N/A

def send_message(account, recipient, message, server):
	with open(account, 'r') as file:
		details = json.load(file)
	with open(recipient, "r") as file:
		destination = json.load(file)
	try:
		print("Sending email message...")
		server.sendmail(details["login"], destination["destination"], message)
		print("Message sent to {} successfully.".format(destination["destination"]))
	except Exception as e:
		print("Exception occured when sending mail: {}".format(e))

############################################################################################
# The following functions have to do with emails to multiple destinations.                 #
############################################################################################

# This ( multiple destination email constructor )
# Takes
# > account: filename of json file with schema
# >> { login:email, password:emailpassword }	
# > recipients: filename of json file with schema
# >> { destinations:[recipientemailaddress1, recipientemailaddress2,...] } 
# > emailmessage: filename of json file with schema
# >> { subject:emailsubjectline, body:emailbodytosend }
# Returns
# > messageContainer: list of email messages according to python MIME library in a list as strings

def construct_message_multiple_destinations(account, recipients, emailmessage):
	try:
		print("Getting details for construction of message...")
		with open(account, 'r') as file:
			details = json.load(file)
		with open(recipients, "r") as file:
			destinations = json.load(file)
		with open(emailmessage, "r") as file:
			message = json.load(file)
		print("Details retrieved successfully.")
	except Exception as e:
		print("An Exception occured when constructing an email message: {} Exiting...".format(e))
		# We want to exit here because if we can't open these files and continue, we will be
		# constructing a bunch of null garbage.
		exit(1)
	numberOfDestinations = len(destinations["destinations"])
	messageContainer = []
	for i in range(numberOfDestinations):
		msg = MIMEMultipart()
		msg['From'] = details["login"]
		msg['To'] = destinations["destinations"][i]
		msg['Subject'] = message["subject"]
		msg.attach(MIMEText(message["body"], 'plain'))
		msg = msg.as_string()
		messageContainer.append(msg)
	return messageContainer


# This ( multiple destination email sender )
# Takes
# > account: filename of json file with schema
# >> { login:email, password:emailpassword }	
# > recipients: filename of json file with schema
# >> { destinations:[recipientemailaddress1, recipientemailaddress2,...] } 
# > messageContainer: string list constructed by python MIME library; returned by construct_message_multiple_destinations
# > server: connection to email SMTP server returned by initializer
# Returns
# N/A

def send_message_multiple_destinations(account, recipients, messageContainer, server):
	with open(account, 'r') as file:
		details = json.load(file)
	with open(recipients, "r") as file:
		destinations = json.load(file)
	numberOfMessages = len(messageContainer)
	for i in range(numberOfMessages):
		try:
			print("Sending email message...")
			server.sendmail(details["login"], destinations["destinations"][i], messageContainer[i])
			print("Message sent to {} successfully.".format(destinations["destinations"][i]))
		except Exception as e:
			print("Exception occured when sending mail: {}".format(e))


###########################################################################################
# The following are other miscellanious functions that can be used as utilities.          #
###########################################################################################

# This ( multiple destination file builder )
# It ( makes a json file that has all of the destinations for an email in the proper schema )
# Takes
# > destinations: a list of strings that are email addresses
# > filename: a string for the filename which will contain the addresses
# Returns
# N/A

def construct_multiple_destinations_file(destinations, filename):
	try:
		print("Making destinations file...")
		data = dict({"destinations":destinations})
		with open(filename, "w") as file:
			json.dump(data, file)
	except Exception as e:
		print("Exception occured when constructing a destinations file: {}".format(e))

# This ( account details file builder )
# It ( builds a json file that has account details for the sender in the proper schema )
# Takes
# > username: a username email string, example@gmail.com
# > password: a password string, mypassword123! -- should be compatible with GMail TODO
# > filename: a string for the filename which will contain the details
# Returns
# N/A
def construct_account_details_file(username, password, filename):
	try:
		print("Making account details file for user {}...".format(username))
		data = dict({"login":username, "password":password})
		with open(filename, "w") as file:
			json.dump(data, file)
	except Exception as e:
		print("Exception occured when constructing an account details file: {}".format(e))



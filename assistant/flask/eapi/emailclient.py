import sys
import smtplib
import json
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


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
		print("Exception occured: {} Exiting...".format(e))
		server.quit()
		exit(1)
	return server

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


# This ( multiple destination email sender )
# Takes
# > account: filename of json file with schema
# >> { login:email, password:emailpassword }	
# > recipients: filename of json file with schema
# >> { destinations:[recipientemailaddress1, recipientemailaddress2,...] } 
# > emailmessage: filename of json file with schema
# >> { subject:emailsubjectline, body:emailbodytosend }
# Returns
# > messages: list of email messages according to python MIME library in a list as strings
def construct_message_multiple_destinations(account, recipients, emailmessage):
	try:
		print("Getting details for construction of message...")
		with open(account, 'r') as file:
			details = json.load(file)
		with open(recipient, "r") as file:
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
	return msg



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



# For now this is a test script to send emails via python
# later I am going to turn it into an API that makes the whole process easier

import smtplib
import json
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


# We need to get our settings from file
account = "accountdetails.cfg"
recipient = "destination.cfg"
emailmessage = "message.email"

# This ( initializer )
# Takes
# > account: json file with schema
# >> { login:email, password:emailpassword }	
# Returns
# N/A
def initialize_client(account, recipient, emailmessage):
	# Set up a server that we can use
	server = smtplib.SMTP('smtp.gmail.com',587)
	with open(account, 'r') as file:
		details = json.load(file)
	# Let's begin talking with the server
	try:
		server.starttls()
		server.login(details["login"], details["password"])
	except Exception as e:
		print("Exception occured: {}".format(e))
		server.quit()

# This ( message builder )
# Takes
# > recipient: json file with schema
# >> { destination:recipientemailaddress )
# > emailmessage: json file with schema
# >> { subject:emailsubjectline, body:emailbodytosend }
# Returns
# > email message according to python MIME lib as string
def construct_message(recipient, emailmessage):
	try:
		with open(recipient, "r") as file:
			destination = json.load(file)
		with open(emailmessage, "r") as file:
			message = json.load(file)
	except Exception as e:
		print("An Exception occured when constructing an email message: {}".format(e))
	msg = MIMEMultipart()
	msg['From'] = details["login"]
	msg['To'] = destination["destination"]
	msg['Subject'] = message["subject"]
	msg.attach(MIMEText(message["body"], 'plain'))
	msg = msg.as_string()
	return msg

try:
	print("Sending email message.")
	server.sendmail(details["login"], destination["destination"], msg)
except Exception as e:
	print("Exception occured: {}".format(e))
finally:
	server.quit()

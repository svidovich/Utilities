#!/usr/bin/env python
# This is a script designed to test the email API.

from emailclient import *

# We need to get our settings from file
account = "accountdetails.cfg"
recipients = "destinations.cfg"
emailmessage = "message.email"
destinations = ["samuel.vidovich@gmail.com", "hannah.appleconnect@gmail.com"]
username = "mydriasis.assistant@gmail.com"
password = "099566421"


# Let's build some files using our API
construct_account_details_file(username, password, account)
construct_multiple_destinations_file(destinations, recipients)

# Next, use our API to send a message!
server = initialize_client(account)
messageContainer = construct_message_multiple_destinations(account, recipients, emailmessage)
send_message_multiple_destinations(account, recipients, messageContainer, server)
close_connection(server)

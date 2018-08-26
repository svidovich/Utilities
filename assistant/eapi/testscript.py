# This is a script designed to test the email API.

from emailclient import *

# We need to get our settings from file
account = "accountdetails.cfg"
recipient = "destination.cfg"
emailmessage = "message.email"

server = initialize_client(account)
message = construct_message(account, recipient, emailmessage)
send_message(message, server)
close_connection(server)

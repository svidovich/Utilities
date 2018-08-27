# This is a script designed to test the email API.

from emailclient import *

# We need to get our settings from file
account = "accountdetails.cfg"
recipients = "destinations.cfg"
emailmessage = "message.email"

# Next, use our API to send a message!
server = initialize_client(account)
messageContainer = construct_message_multiple_destinations(account, recipients, emailmessage)
send_message_multiple_destinations(account, recipients, messageContainer, server)
close_connection(server)

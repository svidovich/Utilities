#!/usr/bin/python

from flask import Flask, request, render_template
import sys
import os
import shutil
from eapi.emailclient import *

app = Flask(__name__, instance_relative_config=True, static_url_path='/static')

@app.route('/assistant')
def form():
    return render_template('form.html')

@app.route('/assistant', methods=['POST'])
def assistant_application():
	account = "./eapi/accountdetails.cfg"
	recipient = "./eapi/destination.cfg"
	emailmessage = "message.email"
	server = initialize_client(account)
	subject = request.form.get('subject')
	body = request.form.get('body')
	with open(emailmessage, 'w') as file:
		file.write('{"subject":"{}", "body":"{}"'.format(subject, body))
	message = construct_message(account, recipient, emailmessage)
	send_message(account, recipient, message, server)
	close_connection(server)
	return "Message sent!"

if __name__ == "__main__":
    app.run()

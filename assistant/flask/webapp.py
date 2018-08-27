#!/usr/bin/python

from flask import Flask, request, render_template
import sys
import os
import shutil
import json
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
	emailsubject = request.form.get('subject')
	emailbody = request.form.get('body')
	emaildata = { "subject":emailsubject, "body":emailbody }
	with open(emailmessage, 'w') as file:
		file.write(json.dumps(emaildata))
	message = construct_message(account, recipient, emailmessage)
	send_message(account, recipient, message, server)
	close_connection(server)
	return "Message sent!"

if __name__ == "__main__":
    app.run()

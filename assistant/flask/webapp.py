#!/usr/bin/python

from flask import Flask, request, render_template
import sys
import os
import shutil
import json
import time
import uuid
from eapi.emailclient import *

app = Flask(__name__, instance_relative_config=True, static_url_path='/static')

@app.route('/assistant')
def form():
    return render_template('form.html')

@app.route('/assistant', methods=['POST'])
def assistant_application():
	options = []
	emailaddress = request.form.get('email')
	if '@' not in emailaddress:
		return "Please use a valid email address."
	if request.form.get('gnosis') is not None:
		options.append(request.form.get('gnosis'))
	if request.form.get('stocks') is not None:
		options.append(request.form.get('stocks'))
	userdetails = {}
	userdetails['email'] = emailaddress
	userdetails['options'] = options
	# TODO Connect a database of users c:
	return "{}".format(userdetails)

if __name__ == "__main__":
    app.run()

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
	options = []
	emailaddress = request.form.get('email')
	options.append(request.form.get('gnosis'))
	options.append(request.form.get('stocks'))
	return "Message sent! {}".format(options)

if __name__ == "__main__":
    app.run()

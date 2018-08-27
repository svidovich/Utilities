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
	usr_entry = request.form.get('text')
	return usr_entry

if __name__ == "__main__":
    app.run()

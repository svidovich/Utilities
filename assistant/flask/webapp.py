#!/usr/bin/python

from flask import Flask, request, render_template
import sys
import os
import shutil

app = Flask(__name__, instance_relative_config=True, static_url_path='/static')

@app.route('/assistant')
def form():
    return render_template('form.html')

if __name__ == "__main__":
    app.run()

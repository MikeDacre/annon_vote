#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A Flask website to make a simple anonymous voting system

       Created: 2016-28-30 21:09
 Last modified: 2016-09-30 22:28

"""
from flask import Flask, render_template

# Create App
app = Flask(__name__)
app.config['DEBUG'] = True


# Views
@app.route('/')
def home():
    """Home page."""
    return render_template('index.html')

@app.route('/admin')
def admin():
    """The backend area."""
    return render_template('admin.html')

if __name__ == "__main__":
    app.run()

"""
This file contains the Application Factory and tells Python that the SATS directory should be treated as a package.
"""
import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    


@app.route('/')
def hello():
    return "Hello, World!"


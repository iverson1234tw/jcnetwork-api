# -*- coding: utf8 -*-
# coding: utf8

from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)

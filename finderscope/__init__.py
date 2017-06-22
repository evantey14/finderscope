from flask import Flask
app = Flask(__name__)

import os
app.config.from_object('config')

from finderscope.models import db
db.app = app
db.init_app(app)

import finderscope.controllers

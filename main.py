from flask import *
from public import public
from admin import admin
from caregiver import caregiver

from api import api


app=Flask(__name__)
app.secret_key="hello"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')

app.register_blueprint(caregiver,url_prefix='/caregiver')
app.register_blueprint(api,url_prefix='/api')


app.run(debug=True,port=5457,host="0.0.0.0")


from crypt import methods
import os
from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY']='004f2af45d3a4e161a7dd2d17fdae47f'
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/sovtech.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    admin = db.Column(db.Boolean)

    def to_dict(self):
        return {
        "public_id": self.public_id,
        "name": self.name,
        "password": self.password,
    }


@app.route('/', methods=["GET", "POST"])
def hello():
    print(request.headers["Authorization"], "man")
    return 'Hello!'

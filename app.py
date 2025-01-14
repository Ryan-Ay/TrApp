from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory, jsonify
from flask_session import Session
from flask_login import LoginManager, UserMixin

import mysql.connector
from mysql.connector import Error
import pandas as pd
import numpy as np
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

import math
import time

import os


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hyungjae1130",
  database="eden"
)

cursor = db.cursor()


app = Flask(__name__)

app.config["SESSION_TYPE"] = "filesystem"

Session(app)


def login_required(f):
    """
    Decorate routes to require login.
    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def login_not_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is not None:
            return redirect("/")
        else:
            return f(*args, **kwargs)
    return decorated_function

@app.route("/", methods=["GET"])
def start():
    return render_template("start.html")

@app.route("/trip", methods=["GET", "POST"])
def trip_code_form():
    if request.method == "GET":
        return render_template("trip_code_form.html")
    else:
        first = request.form["first"]
        second = request.form["second"]
        third = request.form["third"]
        fourth = request.form["fourth"]
        fifth = request.form["fifth"]
        sixth = request.form["sixth"]

        return redirect("/" + first + second + third + fourth + fifth + sixth)
    
@app.route("/<trip_id>", methods=["GET", "POST"])
def student_preference_form(trip_id):
    if request.method == "GET":
        return render_template("student_preference_form.html", trip_id=trip_id)
    else:
        return render_template("success.html", trip_id=trip_id)

@app.route("/teacher-login", methods=["GET", "POST"])
def teacher_login_form():
    if request.method == "GET":
        return render_template("teacher_login_form.html")
    else:
        return redirect("/trips")
    
@app.route("/trips", methods=["GET", "POST"])
def trips():
    if request.method == "GET":
        return render_template("trips.html")

@app.route("/trips/<trip_id>", methods=["GET", "POST"])
def trip(trip_id):
    if request.method == "GET":
        return render_template("trip.html")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3000")
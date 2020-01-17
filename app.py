# import necessary libraries
import os

import json
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/cleaned_team_stats.sqlite"
#DATABASE_URI = 'postgres+psycopg2://postgres:changeme@localhost:5432/team_stats'
#engine = sqlalchemy.create_engine(DATABASE_URI)

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
#print(Base.classes.keys())
Stats = Base.classes.cleaned_team_stats

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/left-sidebar")
def left():
    return render_template("left-sidebar.html")

@app.route("/right-sidebar")
def right():
    return render_template("right-sidebar.html")

@app.route("/no-sidebar")
def none():
    return render_template("no-sidebar.html")

@app.route("/alldata")
def alldata():
    res = db.session.query(Stats.fetchall())
    json.dumps([dict(r) for r in res])

if __name__ == "__main__":
    app.run(debug=True)

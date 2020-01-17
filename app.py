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

#################################################
# Database Setup
#################################################

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/cleaned_team_stats.sqlite"
#DATABASE_URI = 'postgres+psycopg2://postgres:changeme@localhost:5432/team_stats'
#engine = sqlalchemy.create_engine(DATABASE_URI)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/cleaned_team_stats.sqlite"

db = SQLAlchemy(app)

#engine = create_engine("sqlite:///olympicDataFinal.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
#print(Base.classes.keys())
Teamstats = Base.classes.cleaned_team_stats

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/variable")
def variable():
    """Return a list of variable."""

    #Query for the variable
    
    results = db.session.query(Teamstats.variable.distinct().label("variable"))
    variable = [row.variable for row in results.all()]
    returnvariable=[]
    for x in variable:
        if x != None:
            returnvariable.append(x)
    returnvariable.sort(reverse = True)
    
            

    #Return a list of the column names (variable names)
    return jsonify(returnvariable)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/index.html")
def home_1():
    return render_template("index.html")
@app.route("/contact.html")
def contact():
    return render_template('contact.html')
@app.route("/left-sidebar.html")
def left():
    return render_template("left-sidebar.html")
@app.route("/right-sidebar.html")
def right():
    return render_template("right-sidebar.html")
@app.route("/no-sidebar.html")
def none():
    return render_template("no-sidebar.html")


if __name__ == "__main__":
    app.run(debug=True)

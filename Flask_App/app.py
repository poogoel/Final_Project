# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Stats

app = Flask(__name__)

DATABASE_URI = 'postgres+psycopg2://postgres:changeme@localhost:5432/team_stats'
engine = create_engine(DATABASE_URI)
db = SQLAlchemy(app)

Session = sessionmaker(bind=engine)
session = Session()

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/alldata")
def alldata():
    alldata = db.session.query(Stats).all()
    return jsonify(alldata)

if __name__ == "__main__":
    app.run()

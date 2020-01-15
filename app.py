# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
engine = create_engine('postgres+psycopg2://postgres:changeme@localhost:5432/team_stats')


db = SQLAlchemy(app)

from models import Stats

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sys
import json

app = Flask( __name__ )

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql:arn:aws:rds:us-east-2:881778463513:db:dataviz"
db = SQLAlchemy(app)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

DATABASE_URI = 'postgres+psycopg2://postgres:changeme@localhost:5432/team_stats'
engine = sqlalchemy.create_engine(DATABASE_URI)
db = SQLAlchemy(app)

Session = sessionmaker(bind=engine)
session = Session()

class Stats(db.Model):
    __tablename__ = 'team_stats'

    team_id = db.Column(db.Integer, primary_key=True)
    variable = db.Column(db.String())
    first_downs = db.Column(db.Integer)
    first_downs_by_penalty = db.Column(db.Integer)
    third_down_percentage = db.Column(db.Float)
    fourth_down_percentage = db.Column(db.Float)
    average_interception_yards = db.Column(db.Float)
    average_kickoff_return_yards = db.Column(db.Float)
    average_punt_return_yards = db.Column(db.Float)
    interceptions = db.Column(db.Integer)
    net_average_punt_yards = db.Column(db.Float)
    net_passing_yards = db.Column(db.Integer)
    net_passing_yards_per_game = db.Column(db.Float)
    passing_first_downs = db.Column(db.Integer)
    passing_touchdowns = db.Column(db.Integer)
    rushing_first_downs = db.Column(db.Integer)
    rushing_attempts = db.Column(db.Integer)
    rushing_touchdowns = db.Column(db.Integer)
    rushing_yards = db.Column(db.Integer)
    rushing_yards_per_game = db.Column(db.Float)
    total_offensive_plays = db.Column(db.Integer)
    total_points = db.Column(db.Integer)
    total_points_per_game = db.Column(db.Float)
    total_touchdowns = db.Column(db.Integer)
    total_offensive_yards = db.Column(db.Integer)
    yards_per_game = db.Column(db.Float)
    yards_per_pass_attempt = db.Column(db.Float)
    yards_per_rush_attempt = db.Column(db.Float)
    completed_passes = db.Column(db.Integer)
    attempted_passes = db.Column(db.Integer)
    field_goals_completed = db.Column(db.Integer)
    field_goals_attempted = db.Column(db.Integer)
    total_fumbles = db.Column(db.Integer)
    defensive_interception = db.Column(db.Integer)
    yards_after_interception = db.Column(db.Integer)
    total_kickoffs_received = db.Column(db.Integer)
    yards_off_kickoff_received = db.Column(db.Integer)
    total_punts_received = db.Column(db.Integer)
    yards_off_punts_received = db.Column(db.Integer)
    total_punts_kicked = db.Column(db.Integer)
    total_punt_yards = db.Column(db.Integer)
    total_defensive_sacks = db.Column(db.Integer)
    yards_lost_from_sacks = db.Column(db.Integer)
    total_penalties = db.Column(db.Integer)
    total_yards_penalized = db.Column(db.Integer)
    
    def __init__(self, variable,first_downs,first_downs_by_penalty,third_down_percentage,fourth_down_percentage,average_interception_yards,average_kickoff_return_yards,average_punt_return_yards,interceptions,net_average_punt_yards,net_passing_yards,net_passing_yards_per_game,passing_first_downs,passing_touchdowns,rushing_first_downs,rushing_attempts,rushing_touchdowns,rushing_yards,rushing_yards_per_game,total_offensive_plays,total_points,total_points_per_game,total_touchdowns,total_offensive_yards,yards_per_game,yards_per_pass_attempt,yards_per_rush_attempt,completed_passes,attempted_passes,field_goals_completed,field_goals_attempted,total_fumbles,defensive_interception,yards_after_interception,total_kickoffs_received,yards_off_kickoff_received,total_punts_received,yards_off_punts_received,total_punts_kicked,total_punt_yards,total_defensive_sacks,yards_lost_from_sacks,total_penalties,total_yards_penalized):
        self.variable = variable
        self.first_downs = first_downs
        self.first_downs_by_penalty = first_downs_by_penalty
        self.third_down_percentage = third_down_percentage
        self.fourth_down_percentage = fourth_down_percentage 
        self.average_interception_yards = average_interception_yards
        self.average_kickoff_return_yards = average_kickoff_return_yards
        self.average_punt_return_yards = average_punt_return_yards
        self.interceptions = interceptions
        self.net_average_punt_yards = net_average_punt_yards
        self.net_passing_yards = net_passing_yards
        self.net_passing_yards_per_game = net_passing_yards_per_game
        self.passing_first_downs = passing_first_downs
        self.passing_touchdowns = passing_touchdowns
        self.rushing_first_downs = rushing_first_downs
        self.rushing_attempts = rushing_attempts
        self.rushing_touchdowns = rushing_touchdowns
        self.rushing_yards = rushing_yards
        self.rushing_yards_per_game = rushing_yards_per_game
        self.total_offensive_plays = total_offensive_plays
        self.total_points = total_points
        self.total_points_per_game = total_points_per_game 
        self.total_touchdowns = total_touchdowns
        self.total_offensive_yards = total_offensive_yards
        self.yards_per_game = yards_per_game
        self.yards_per_pass_attempt = yards_per_pass_attempt
        self.yards_per_rush_attempt = yards_per_rush_attempt
        self.completed_passes = completed_passes
        self.attempted_passes = attempted_passes
        self.field_goals_completed = field_goals_completed
        self.field_goals_attempted = field_goals_attempted
        self.total_fumbles = total_fumbles
        self.defensive_interception = defensive_interception
        self.yards_after_interception = yards_after_interception
        self.total_kickoffs_received = total_kickoffs_received
        self.yards_off_kickoff_received = yards_off_kickoff_received
        self.total_punts_received = total_punts_received
        self.yards_off_punts_received = yards_off_punts_received
        self.total_punts_kicked = total_punts_kicked
        self.total_punt_yards = total_punt_yards
        self.total_defensive_sacks = total_defensive_sacks
        self.yards_lost_from_sacks = yards_lost_from_sacks
        self.total_penalties = total_penalties
        self.total_yards_penalized = total_yards_penalized
    
    def __repr__(self):
        return '<team_id {}>'.format(self.team_id)

@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()

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
    alldata = db.session.query(Stats).all()
    return jsonify(alldata)

if __name__ == "__main__":
    app.run()

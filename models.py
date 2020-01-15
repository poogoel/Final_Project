### models.py ###

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Stats(Base):
    __tablename__ = 'team_stats'
    team_id = Column(Integer, primary_key=True)
    variable = Column(String)
    first_downs = Column(Integer)
    first_downs_by_penalty = Column(Integer)
    third_down_percentage = Column(Float)
    fourth_down_percentage = Column(Float)
    average_interception_yards = Column(Float)
    average_kickoff_return_yards = Column(Float)
    average_punt_return_yards = Column(Float)
    interceptions = Column(Integer)
    net_average_punt_yards = Column(Float)
    net_passing_yards = Column(Integer)
    net_passing_yards_per_game = Column(Float)
    passing_first_downs = Column(Integer)
    passing_touchdowns = Column(Integer)
    rushing_first_downs = Column(Integer)
    rushing_attempts = Column(Integer)
    rushing_touchdowns = Column(Integer)
    rushing_yards = Column(Integer)
    rushing_yards_per_game = Column(Float)
    total_offensive_plays = Column(Integer)
    total_points = Column(Integer)
    total_points_per_game = Column(Float)
    total_touchdowns = Column(Integer)
    total_offensive_yards = Column(Integer)
    yards_per_game = Column(Float)
    yards_per_pass_attempt = Column(Float)
    yards_per_rush_attempt = Column(Float)
    completed_passes = Column(Integer)
    attempted_passes = Column(Integer)
    field_goals_completed = Column(Integer)
    field_goals_attempted = Column(Integer)
    total_fumbles = Column(Integer)
    defensive_interception = Column(Integer)
    yards_after_interception = Column(Integer)
    total_kickoffs_received = Column(Integer)
    yards_off_kickoff_received = Column(Integer)
    total_punts_received = Column(Integer)
    yards_off_punts_received = Column(Integer)
    total_punts_kicked = Column(Integer)
    total_punt_yards = Column(Integer)
    total_defensive_sacks = Column(Integer)
    yards_lost_from_sacks = Column(Integer)
    total_penalties = Column(Integer)
    total_yards_penalized = Column(Integer)
    
    def __repr__(self):
        return "<Stats(team_id={}, variable='{}', first_downs={}, first_downs_by_penalty={}, third_down_percentage={}, fourth_down_percentage={}, average_interception_yards={}, average_kickoff_return_yards={}, average_punt_return_yards={}, interceptions={}, net_average_punt_yards={}, net_passing_yards={}, net_passing_yards_per_game={}, passing_first_downs={}, passing_touchdowns={}, rushing_first_downs={}, rushing_attempts={}, rushing_touchdowns={}, rushing_yards={}, rushing_yards_per_game={}, total_offensive_plays={}, total_points={}, total_points_per_game={}, total_touchdowns={}, total_offensive_yards={}, yards_per_game={}, yards_per_pass_attempt={}, yards_per_rush_attempt={}, completed_passes={}, attempted_passes={}, field_goals_completed={}, field_goals_attempted={}, total_fumbles={}, defensive_interception={}, yards_after_interception={}, total_kickoffs_received={}, yards_off_kickoff_received={}, total_punts_received={}, yards_off_punts_received={}, total_punts_kicked={}, total_punt_yards={}, total_defensive_sacks={}, yards_lost_from_sacks={}, total_penalties={}, total_yards_penalized={})>"\
                .format(self.team_id, self.variable, self.first_downs, self.first_downs_by_penalty, self.third_down_percentage, self.fourth_down_percentage, self.average_interception_yards, self.average_kickoff_return_yards, self.average_punt_return_yards, self.interceptions, self.net_average_punt_yards, self.net_passing_yards, self.net_passing_yards_per_game, self.passing_first_downs, self.passing_touchdowns, self.rushing_first_downs, self.rushing_attempts, self.rushing_touchdowns, self.rushing_yards, self.rushing_yards_per_game, self.total_offensive_plays, self.total_points_per_game, self.total_touchdowns, self.total_offensive_yards, self.yards_per_game, self.yards_per_pass_attempt, self.yards_per_rush_attempt, self.completed_passes, self.attempted_passes, self.field_goals_completed, self.field_goals_attempted, self.total_fumbles, self.defensive_interception, self.yards_after_interception, self.total_kickoffs_received, self.yards_off_kickoff_received, self.total_punts_received, self.yards_off_punts_received, self.total_punts_kicked, self.total_punt_yards, self.total_defensive_sacks, self.yards_lost_from_sacks, self.total_penalties, self.total_yards_penalized)
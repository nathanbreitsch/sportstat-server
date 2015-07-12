from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sportstat.database import Base


class Team(Base):
    __tablename__ = 'Team'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    city = Column(String(80))
    state = Column(String(2))

    @property
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state
        }

class Athlete(Base):
    __tablename__ = 'Athlete'
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('Team.id'), nullable=False)
    team = relationship(Team)
    position = Column(String(2), nullable=False)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)

    @staticmethod
    def create(data):
        #return data
        assert(data.has_key('first_name'))
        assert(data.has_key('last_name'))
        assert(data.has_key('position'))
        assert(data.has_key('team_id'))

        athlete = Athlete(
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            position = data.get('position'),
            team_id = data.get('team_id')
        )
        return athlete

    @property
    def serialize(self):
        return{
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'team_name': self.team.name,
            'team_id': self.team_id
        }

class Game(Base):
    __tablename__ = 'Game'
    id = Column(Integer, primary_key=True)

    home_team_id = Column(Integer, ForeignKey('Team.id'))
    home_team = relationship(Team, foreign_keys=home_team_id)
    away_team_id = Column(Integer, ForeignKey('Team.id'))
    away_team = relationship(Team, foreign_keys=away_team_id)
    datetime = Column(DateTime)
    location = Column(String(80))

    @property
    def serialize(self):
        return{
            'id': self.id,
            'home_team_id': self.home_team_id,
            'away_team_id': self.away_team_id,
            'datetime': self.datetime,
            'location': self.location
        }

class Play(Base):
    __tablename__ = 'Play'

    id = Column(Integer, primary_key=True)

    play_index = Column(Integer, nullable=False)
    quarter_index = Column(Integer, nullable=False)
    down = Column(Integer, nullable = False)
    offense_id = Column(Integer, ForeignKey('Team.id'), nullable=False)
    offense = relationship(Team, foreign_keys=offense_id)
    defense_id = Column(Integer, ForeignKey('Team.id'), nullable=False)
    defense = relationship(Team, foreign_keys=defense_id)
    half = Column(Boolean)
    yards = Column(Integer)
    result = Column(String(40))

    @property
    def serialize(self):
        return{
            'id': self.id,
            'play_index': self.play_index,
            'quarter_index': self.quarter_index,
            'down': self.down,
            'offense_id': self.offense_id,
            'defense_id': self.defense_id,
            'half': self.half,
            'yards': self.yards,
            'result': self.result
        }

class Action(Base):
    __tablename__ = 'Action'

    id = Column(Integer, primary_key=True)
    action_type = Column(String(80), nullable=False)
    player_id = Column(Integer, ForeignKey('Athlete.id'))
    player = relationship(Athlete)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'player_id': self.away_team_id
        }

class Observation(Base):
    __tablename__ = 'Observation'

    id = Column(Integer, primary_key=True)
    action_id = Column(Integer, ForeignKey('Action.id'))
    action = relationship(Action)
    name = Column(String(40))
    value = Column(String(80))

    @property
    def serialize(self):
        return{
            'id': self.id,
            'action_id': self.action_id,
            'name': self.name,
            'value': self.value
        }


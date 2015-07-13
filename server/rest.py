from server import app
from sportstat.database import session
from sportstat.models import Team, Athlete, Game, Play, Action, Observation


@app.route('/help', methods=['GET'])
def api_help():
    '''
    Return help message and API usage/documentation.
    '''
    return '''<h1>Help Page</h1>'''

@app.route('/sportstat/api/v0.1/athletes', methods=['GET'])
def get_athletes():
    '''
    Return all athlete data in json format.
    '''
    athletes = [athlete.serialize for athlete in session.query(Athlete)]
    return jsonify(athletes)

#@app.route('/sportstat/api/v0.1/athletes/<last>', methods=['GET'])
@app.route('/sportstat/api/v0.1/athletes/<first>-<last>', methods=['GET'])
def get_athlete_by_name(last, first=None):
    '''
    Return data in json format for athlete with corresponding name.
    '''
    # TODO how to make queries
    athletes = [athlete.serialize for athlete in session.query(Athlete).filter(first=first, last=last)]
    return jsonify(athletes)

#@app.route('/sportstat/api/v0.1/athletes/<team>-<int:number>', methods=['GET'])
@app.route('/sportstat/api/v0.1/athletes/<team>-<int:number>-<date>', methods=['GET'])
def get_athlete_by_team_number_date(team, number, date=None):
    '''
    Return data in json format for athlete with corresponding team and number.
    Optional date parameter can help resolve ambiguity.
    '''
    # TODO date and team name validation, handling errors
    athletes = [athlete.serialize for athlete in session.query(Athlete).filter(team=team, number=number)]
    return jsonify(athletes)



@app.route('/sportstat/api/v0.1/teams', methods=['GET'])
def get_teams():
    '''
    Return all team data in json format.
    '''
    teams = [team.serialize for team in session.query(Team)]
    return jsonify(teams)



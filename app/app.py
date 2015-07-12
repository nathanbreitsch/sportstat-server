from flask import Flask, request, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Team, Athlete

engine = create_engine('sqlite:///sports.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

def getQuery(request):
    if request.method == 'GET':
        query = request.args
    elif request.method == 'POST':
        query = request.form
    return query

def getSelection(table_class, query):
    selection = session.query(table_class)
    #return jsonify(vals = [query.getlist(key) for key in query.keys()])
    for param in query.keys():
        if param in table_class.__dict__:
            selection = selection.filter(table_class.__dict__[param].in_(query.getlist(param)))
    return selection

#get all athletes
@app.route('/api/find/athlete', methods=['GET', 'POST'])
def getAthletes():
    query = getQuery(request)
    athletes = getSelection(Athlete, query)
    return jsonify(athletes = [a.serialize for a in athletes])


@app.route('/api/find/team', methods=['GET', 'POST'])
def getTeams():
    query = getQuery(request)
    teams = getSelection(Team, query)
    return jsonify(teams = [i.serialize for i in teams])

@app.route('/api/create/athlete', methods=['POST'])
def createAthlete():
    data = request.form
    athlete = Athlete.create(data)
    session.add(athlete)
    session.commit()
    return jsonify(athlete.serialize)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '127.0.0.1', port=1337)

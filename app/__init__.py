from flask import Flask, request, jsonify
app = Flask(__name__)

from sportstat.database import init_db, session
from sportstat.models import Team, Athlete, Game, Play, Action, Observation
# call to sync models to database
init_db()

# it is important that all route modules are imported from this `__init__` 
# file, so they are registered with flask.
import app.rest

@app.teardown_appcontext
def shutdown_session(exception=None):
    '''
    Flask should automatically call this function when the application shuts
    down in order to remove all database sessions.
    '''
    session.remove()

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=3000)

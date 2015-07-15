from flask import Flask
app = Flask(__name__)

from sportstat.database import init_db, session
from sportstat.models import Team, Athlete, Game, Play, Action, Observation
# call to sync models to database
init_db()

# It is important that all route modules are imported from this `__init__` 
# file, so they are registered with flask.
# Circular imports are normally a bad idea. See 
# [this post](https://support.google.com/docs/answer/186103?hl=en)
import rest

@app.teardown_appcontext
def shutdown_session(exception=None):
    '''
    Flask should automatically call this function when the application shuts
    down in order to remove all database sessions.
    '''
    session.remove()


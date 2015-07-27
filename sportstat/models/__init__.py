# init for models module
# This module is imported by sportstat.database before initializing the
# database in `init_db`. As such, all modules that should be present in the
# database must be imported by this file.
from sportstat.models.models import Team, Athlete, Game, Play, Action, Observation

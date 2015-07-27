from sportstat.database import init_db, session
from sportstat.models import Team, Athlete, Game, Play, Action, Observation
#init_db()  # __dbname__ not defined; using in-memory sqlite

def create_teams(path_to_teams):
    file = open(path_to_teams, 'r')
    teams = [line.split(',') for line in file.readlines()]
    file.close()

    for team in teams[1:]:#first line is column names
        #make and commit team
        team_record = Team()
        team_record.name = team[1]
        session.add(team_record)
        file.close()
    session.commit()
    #session.close()

def list_teams():
    for team in session.query(Team).all():
        print(team.name)

if __name__ == '__main__':
    create_teams('../../data/teams.csv')
    session.close()

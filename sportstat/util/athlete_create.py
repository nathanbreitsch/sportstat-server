from sportstat.database import init_db, session
from sportstat.models import Team, Athlete, Game, Play, Action, Observation
#init_db()  # __dbname__ not defined; using in-memory sqlite

def create_athletes(path_to_teams):
    teams = session.query(Team).all()
    for team in teams:
        team_name = '_'.join(team.name.split(' '))
        file = open(path_to_data_dir + '/rosters/' + team_name + '.txt', 'r')
        for line in file.readlines():
            first_name, last_name, suffix, position, height, weight, year = line.split(',')
            #make and commit athlete
            athlete = Athlete()
            athlete.first_name = first_name
            athlete.last_name = last_name
            athlete.suffix = suffix
            athlete.position = position
            athlete.height = height
            athlete.weight = weight
            athlete.year = year
            athlete.team_id = team.id

            session.add(athlete)
    session.commit()


def check_athletes():
    print(session.query(Athlete).count())

if __name__ == '__main__':
    create_athletes('../../data/teams.csv')
    session.close()

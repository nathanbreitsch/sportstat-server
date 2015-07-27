from sportstat.database import init_db, session
from sportstat.models import Team, Athlete, Game, Play, Action, Observation
#init_db()  # __dbname__ not defined; using in-memory sqlite

def create_games(path_to_games_list):
    #for now we just do sugar bowl
    osu = session.query(Team).filter_by(name='Ohio State').one()
    bama = session.query(Team).filter_by(name='Alabama').one()
    game = Game()
    game.home_team_id = osu.id
    game.away_team_id = bama.id
    session.add(game)
    session.commit()
    
def check_games():
    print(session.query(Game).count())

if __name__ == '__main__':
    create_games('../../data/games.csv')
    session.close()

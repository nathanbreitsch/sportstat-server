from sportstat.database import init_db, session
from sportstat.models import Team, Athlete, Game, Play, Action, Observation
#init_db()  # __dbname__ not defined; using in-memory sqlite



def create_plays(path_to_game_file):
    osu = session.query(Team).filter(Team.name == 'Ohio State').one()
    bama = session.query(Team).filter(Team.name == 'Alabama').one()

    decode_def_off = {
        'OSU': osu,
        'BAMA': bama
    }

    game = session.query(Game).one()

    file = open(path_to_game_file,'r')
    lines = file.readlines()
    for line in lines[2:]:#first two lines are meta
        cols = line.split(',')
        if cols[0].strip() != '':
            play_index = cols[0].strip()
            offense_code = cols[1].strip()
            print(offense_code)
            defense_code = cols[2].strip()
            offense = decode_def_off[offense_code]
            defense = decode_def_off[defense_code]
            quarter = int(cols[3].strip())
            down = int(cols[4].strip())
            print(offense.id)
            #yards_to_go = int(cols[5].strip())
            half = cols[6].strip()
            yards = cols[7].strip()
            result = cols[8].strip()

            play = Play()
            play.game_id = game.id
            play.play_index = int(play_index)
            play.quarter_index = int(quarter)
            play.offense_id = offense.id
            play.defense_id = defense.id
            play.down = down
            #play.yards_to_go = yards_to_go
            play.half = bool(half == 'Own')
            play.yards = int(yards)
            play.result = result
            session.add(play)
    session.commit()
    file.close()


def check_plays():
    print(session.query(Athlete).count())

if __name__ == '__main__':
    create_plays('../../data/teams.csv')
    session.close()

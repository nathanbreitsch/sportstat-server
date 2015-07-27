from sportstat.database import init_db, session
from sportstat.models import Team, Athlete, Game, Play, Action, Observation
#init_db()  # __dbname__ not defined; using in-memory sqlite

def create_qb_actions(path_to_game_file):
    #get quarterback actions
    file = open(path_to_game_file,'r')
    lines = file.readlines()
    for line in lines[2:]:#first two lines are meta
        cols = line.split(',')
        if cols[0].strip() != '':
            play_index = cols[0].strip()
            game_id = 1
            play_id = session.query(Play)\
                .join(Game)\
                .filter(Play.play_index == play_index)\
                .filter(Game.id == game_id)\
                .one().id
            offense_code = cols[1].strip()
            offense = decode_def_off[offense_code]
        quarterback = cols[9].strip()
        if quarterback != '':
            first_name, last_name, number = quarterback.split(' ')
            first_name = first_name.strip()
            last_name = last_name.strip()
            sguc = cols[10].strip()
            alt = cols[11].strip()
            comp = cols[12].strip()
            direction = cols[13].strip()
            air_yards = cols[14].strip()
            total_yards = cols[15].strip()
            press = cols[16].strip()
            pock = cols[17].strip()
            scram = cols[18].strip()

            qb = session.query(Athlete).filter(Athlete.position == 'QB')
            qb = qb.filter(Athlete.first_name == first_name)
            qb = qb.filter(Athlete.last_name == last_name)
            try:
                qb = qb.one()
            except:
                print('no matching qb for ' + first_name + ' ' + last_name)
            else:
                qb_action = Action()
                qb_action.play_id = play_id
                qb_action.athlete_id = qb.id
                qb_action.action_type = 'QB'
                session.add(qb_action)
    session.commit()

    file.close()


def check_qb_actions():
    print(session.query(Athlete).count())

if __name__ == '__main__':
    create_qb_actions('../../data/teams.csv')
    session.close()

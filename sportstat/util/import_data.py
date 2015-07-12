from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Team, Athlete

engine = create_engine('sqlite:///sports.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

osu = Team(name = "Buckeyes",
            city = "Columbus",
            state = "Ohio")
session.add(osu)


bama = Team(name = "Alabama",
            city = "Who",
            state = "Cares")
session.add(bama)

session.commit()

file = open("app/data/osu_roster.csv","r")
for line in file.readlines():
    words = line.split("\t")
    (last_name, first_name) = words[2].split(",")
    first_name = first_name.strip()
    position = words[3]
    playa = Athlete(first_name = first_name,
                    last_name = last_name,
                    position = position,
                    team_id = osu.id)
    session.add(playa)
file.close()

file = open("app/data/alabama_roster.csv","r")
for line in file.readlines():
    words = line.split("\t")
    name_city = words[1].split(" ")
    position = words[2]
    first_name = name_city[0]
    last_name = name_city[1]
    playa = Athlete(first_name = first_name,
                    last_name = last_name,
                    position = position,
                    team_id = bama.id)
    session.add(playa)
file.close()
session.commit()

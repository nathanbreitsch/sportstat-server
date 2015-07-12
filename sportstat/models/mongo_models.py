from mongoengine import Document, IntField, FloatField, StringField, DateTimeField


STATES_AND_PROVINCES = (
        'AL', 'AK', 'AZ', 'AR', 'CA',
        'CO', 'CT', 'DE', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA',
        'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO',
        'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH',
        'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT',
        'VA', 'WA', 'WV', 'WI', 'WY',
        
        'AS', 'DC', 'FM', 'GU', 'MH',
        'MP', 'PW', 'PR', 'VI', 'AE',
        'AA', 'AE', 'AP')

POSITIONS = (
        ('QB', 'quarterback'),
        ('TE', 'tight end'),
        )

class Team(Document):
    name = StringField(primary_key=True, unique=True, max_length=80, nullable=False)
    city = StringField(max_length=80)
    state = StringField(choices=STATES_AND_PROVINCES)
    roster = ListField(ReferenceField(Athlete), default=list)


class Athlete(Document):
    team = ReferenceField(Team)
    position = StringField(choices=POSITIONS)
    first_name = StringField(max_length=80, required=True)
    last_name = StringField(max_length=80, required=True)


class Game(Document):
    home_team = ReferenceField(Team)
    away_team = ReferenceField(Team)
    datetime = DateTimeField()
    location = StringField(max_length=80)


class Play(Document):
    play_index = IntField(required=True)
    quarter_index = IntField(required=True)
    down = IntField(required=True)
    offense = ReferenceField(Team)
    defense = ReferenceField(Team)
    half = BooleanField()
    yards = IntField()
    result = StringField(max_length=40)


class Action(Document):
    action_type = StringField(max_length=80)
    player = ReferenceField(Athlete)
    observations = ListField(Observation(), default=list)


class Observation(Document):
    name = StringField(max_length=40)
    value = StringField(max_length=80)


'''
sql_database.py

Sets up SQLAlchemy engine and declares model `Base`.
Design from:
http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/

Call `init_db()` from application before using database.
To use a database other than an in-memory default, set `__dbname__` to the
correct database url at the global scope before importing this module.

    __dbname__ = 'sqlite:////tmp/test.db'
    from sportstat.database import session, init_db
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#this doesn't work because...
#if '__dbname__' not in globals():
#    __dbname__ = 'sqlite://'

#probs will only be one db anyway during dev
__dbname__ = 'sqlite:////tmp/test.db'

engine = create_engine(__dbname__, convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import sportstat.models
    Base.metadata.create_all(bind=engine)

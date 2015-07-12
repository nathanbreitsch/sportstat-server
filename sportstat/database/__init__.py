'''
init for database module

This is for using SQLAlchemy. The application or user should import `init_db`
and `session`, then call `init_db()` before using `session` to query the DB.

The mongo equivalent would be to ignore this module and instead import
models from application before calling:

    from mongoengine import connect
    connect(name, hostname, port)

The mongo models will then behave as expected.
'''

from sportstat.database.sql_database import Base, init_db, session


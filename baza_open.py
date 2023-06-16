# import sqlite3
# import pandas as pd
#
# conn = sqlite3.connect('european_database.sqlite')
#
# query = """
# SELECT
#     m.*, d.name, d.country
# FROM matchs m
# JOIN divisions d ON d.division == m.Div
# """
#
# df = (
#     pd.read_sql_query(query, conn)
#     .assign(Date=lambda x: pd.to_datetime(x.Date))
# )
# print(df.head())
import sqlalchemy as db

# engine = db.create_engine('sqlite:///european_database.sqlite')
# conn = engine.connect()
#
# metadata = db.MetaData()
# division = db.Table('divisions', metadata, autoload_with=engine)
# print(repr(metadata.tables['divisions']))
# print(division.columns.keys())
# query = division.select()
#
# exe = conn.execute(query)
# result = exe.fetchmany(10)
# print(result[0])
#
# for row in result:
#     print(row)


engine = db.create_engine('sqlite:///datacamp.sqlite')
conn = engine.connect()
metadata = db.MetaData()

Student = db.Table('Student', metadata,
                   db.Column('id', db.Integer(), primary_key=True),
                   db.Column('name', db.String(255), nullable=False),
                   db.Column('major', db.String(255), default='Computer Science'),
                   db.Column('pass', db.Boolean(), default=True))

# metadata.create_all(engine)

query = db.insert(Student).values(name='Ravi', major='Math')
ResultProxy = conn.execute(query)

query = db.insert(Student)
values_list = [{'name': 'Nisha', 'major': "Science", 'pass': False},
               {'name': 'Natasha', 'major': "Math", 'pass': True},
               {'name': 'Ben', 'major': "English", 'pass': False}]

# output = Student.select().where(Student.columns.major == 'Math')
# output2 = Student.select().where(Student.columns.name.like('N%'))
# output3 = Student.select().where(Student.columns.name.in_(['Nisha', 'Ben']))
# output4 = Student.select().where(Student.columns.name.between('Nisha', 'Ravi'))
# output5 = Student.select().where(Student.columns.name.contains('Natasha'))
# output6 = Student.select().where(Student.columns.name.startswith('N'))
# output7 = Student.select().where(Student.columns.name.endswith('a'))
# output8 = Student.select().where(Student.columns.name.is_(None))
# output9 = Student.select().where(Student.columns.name.isnot(None))
# output10 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name)
# output11 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.desc())
# output12 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc())
output13 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc()
, Student.columns.major.desc())
output14 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(),
                                                                             Student.columns.major.desc()).limit(2)
# output15 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1)
# output16 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1).distinct()
# output17 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1).distinct(Student.columns.name)
# output18 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1).distinct(Student.columns.name).with_only_columns([Student.columns.name, Student.columns.major])
# output19 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1).distinct(Student.columns.name).with_only_columns([Student.columns.name, Student.columns.major]).where(Student.columns.major == 'Math')
# output20 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1).distinct(Student.columns.name).with_only_columns([Student.columns.name, Student.columns.major]).where(Student.columns.major == 'Math').where(Student.columns.name == 'Nisha')
# output21 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1).distinct(Student.columns.name).with_only_columns([Student.columns.name, Student.columns.major]).where(Student.columns.major == 'Math').where(Student.columns.name == 'Nisha').where(Student.columns.pass_ is True)
# output22 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1).distinct(Student.columns.name).with_only_columns([Student.columns.name, Student.columns.major]).where(Student.columns.major == 'Math').where(Student.columns.name == 'Nisha').where(Student.columns.pass_ is True).where(Student.columns.id == 1)
# output23 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1).distinct(Student.columns.name).with_only_columns([Student.columns.name, Student.columns.major]).where(Student.columns.major == 'Math').where(Student.columns.name == 'Nisha').where(Student.columns.pass_ is True).where(Student.columns.id == 1).where(Student.columns.id == 2)
# output24 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1).distinct(Student.columns.name).with_only_columns([Student.columns.name, Student.columns.major]).where(Student.columns.major == 'Math').where(Student.columns.name == 'Nisha').where(Student.columns.pass_ is True).where(Student.columns.id == 1).where(Student.columns.id == 2).where(Student.columns.id == 3)
# output25 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1).distinct(Student.columns.name).with_only_columns([Student.columns.name, Student.columns.major]).where(Student.columns.major == 'Math').where(Student.columns.name == 'Nisha').where(Student.columns.pass_ is True).where(Student.columns.id == 1).where(Student.columns.id == 2).where(Student.columns.id == 3).where(Student.columns.id == 4)
output26 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(),
                                                                             Student.columns.major.desc()).limit(2).offset(1).distinct(Student.columns.name).with_only_columns([Student.columns.name, Student.columns.major]).where(Student.columns.major == 'Math').where(Student.columns.name == 'Nisha').where(Student.columns.pass_ is True).where(Student.columns.id == 1).where(Student.columns.id == 2).where(Student.columns.id == 3).where(Student.columns.id == 4).where(Student.columns.id == 5)
# output27 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1)
# output28 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1).with_only_columns([Student.columns.name, Student.columns.major])
# output29 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(), Student.columns.major.desc()).limit(2).offset(1).with_only_columns([Student.columns.name, Student.columns.major]).where(Student.columns.major == 'Math')
# output30 = Student.select().where(Student.columns.name.isnot(None)).order_by(Student.columns.name.asc(),
#                                                                              Student.columns.major.desc()).limit(2).offset(1).with_only_columns([Student.columns.name,
#                                                                                                                                                  Student.columns.major]).where(Student.columns.major == 'Math').where(Student.columns.name == 'Nisha')
Result = conn.execute(query, values_list)
# output = conn.execute(Student.select()).fetchall()
ex = conn.execute(output26)
print(ex.fetchall())

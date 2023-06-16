import sqlite3

import datetime as dt
import numpy as np
import pandas as pd
import requests

data = np.genfromtxt('data/example_data.csv', delimiter=';', encoding='UTF', dtype=None)
# print(data)

array_dict = {
    col: np.array([row[i] for row in data])
    for i, col in enumerate(data[0])
}

df = pd.DataFrame(array_dict)
# df.to_excel('data/example_data.xlsx', index=False)

# df2 = pd.read_csv('data/parsed.csv', sep=';', encoding='UTF')
# df2.to_json('data/parsed2.json', orient='records')


with sqlite3.connect('data/quakes.db') as conn:
    qu = pd.read_sql('SELECT * FROM tsunamis', conn)

# print(qu.head())

yesterday = dt.date.today() - dt.timedelta(days=1)
api = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
payload = {
    'format': 'geojson',
    'starttime': yesterday - dt.timedelta(days=30),
    'endtime': yesterday
}
response = requests.get(api, params=payload)

f = response.json()
# print(f['features'][0])

earthquakes_data = [
    quake['properties']
    for quake in f['features']
]
df3 = pd.DataFrame(earthquakes_data)
print(df3.info())

# df3[['mag', 'title']][100:1500].to_excel('data/earthquakes.xlsx')
# df3[df3.mag >= 7.0].to_excel('data/earthquakes.xlsx')
df3.loc[(df3.tsunami == 1) & (df3.alert == 'green'), ['alert', 'mag', 'title']].to_excel('data/earthquakes.xlsx')

import pandas as pd
data = pd.read_csv('2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
# print(data.head())
# print(data.info())

print(data['Primary Fur Color'].count())
dat= data['Primary Fur Color'].value_counts()

dat.to_csv('data.csv')
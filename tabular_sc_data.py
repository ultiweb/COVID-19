import glob

import pandas as pd
import numpy as np
import os

csv_files = os.path.abspath(os.path.join(os.path.dirname(__file__), 'csse_covid_19_data/csse_covid_19_daily_reports/*.csv'))
# print('fn variable:', csv_files)

latest_file = max(glob.iglob(csv_files), key=os.path.basename)
# print('latest file:', latest_file)

df = pd.read_csv(latest_file, index_col=0)

df = df.sort_index()
df = df.loc[45001:45091, ['Combined_Key', 'Confirmed', 'Deaths', 'Last_Update']]
df['Last_Update'] = pd.to_datetime(df['Last_Update']).dt.strftime('%m/%d/%Y %I:%M %p')

df2 = df.sort_values(by=['Confirmed', 'Deaths'], ascending=False)

df2['DeathRate'] = round(100 * (df2['Deaths'] / df2['Confirmed']), 2)
# df2['DeathRate'] = str(df2['DeathRate'])

df2['Sum'] = df2.sum(axis=0)

df2 = df2[['Last_Update', 'Combined_Key', 'Confirmed', 'Deaths', 'DeathRate']]

df2.columns = ['Updated', 'City, State, Country', 'Confirmed Cases', 'Deaths', '% Lethality']

print(df2.to_string(index=False))

df3 = df2.sum(axis=0)
print(df3)

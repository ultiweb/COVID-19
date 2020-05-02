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

df = df.sort_values(by=['Confirmed', 'Deaths'], ascending=False)

df['DeathRate'] = round(100 * (df['Deaths'] / df['Confirmed']), 2)
# df2['DeathRate'] = str(df2['DeathRate'])
df['EstimatedCases'] = 8 * df['Confirmed']
df['ActualLethality'] = round(100 * (df['Deaths'] / df['EstimatedCases']), 2)

df = df[['Last_Update', 'Combined_Key', 'Confirmed', 'Deaths', 'DeathRate', 'EstimatedCases', 'ActualLethality']]

df.columns = ['Updated', 'City, State, Country', 'Confirmed', 'Deaths', '% Lethality', 'Estimated', '% Estimated Lethality']

print(df.to_string(index=False))

# df2 = df
df2 = df.sum(axis=0)
# df2 = df2.loc['Confirmed', 'Deaths', 'DeathRate', 'EstimatedCases', 'ActualLethality']
# df2 = df2[['Confirmed', 'Deaths', 'DeathRate']]
df2['% Lethality'] = df2['% Lethality'] / len(df)
df2['% Estimated Lethality'] = df2['% Estimated Lethality'] / len(df)
print(df2.to_string(index=True))

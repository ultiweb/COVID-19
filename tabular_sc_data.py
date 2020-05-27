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
df['EstimatedCases'] = round(7.1428 * df['Confirmed'], 0)
df['ActualLethality'] = round(100 * (df['Deaths'] / df['EstimatedCases']), 2)

df = df[['Last_Update', 'Combined_Key', 'Confirmed', 'Deaths', 'DeathRate', 'EstimatedCases', 'ActualLethality']]

df.columns = ['Updated', 'City, State, Country', 'Confirmed', 'Deaths', '% Lethality', 'Estimated', '% Estimated Lethality']

# display estimated values floats as ints
cols = ['Estimated']
df[cols] = df[cols].applymap(np.int64)
print(df.to_string(index=False))
# Below reformats floats as ints although they remain as float values in the DataFrame
# pd.options.display.float_format = '{:,.0f}'.format

# Print summary at bottom
df2 = df.sum(axis=0)
df2['% Lethality'] = round(df2['% Lethality'] / len(df), 2)
df2['% Estimated Lethality'] = round((df2['% Estimated Lethality'] / len(df)), 2)

print(df2.iloc[2:].to_string(index=True))

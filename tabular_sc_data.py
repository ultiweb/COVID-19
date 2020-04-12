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

df.columns = ['City, State, Country', 'Confirmed Cases', 'Deaths', 'Updated']

print(df.to_string(index=False))

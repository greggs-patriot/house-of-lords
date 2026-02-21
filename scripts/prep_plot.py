import os
import pandas as pd

IN_PATH = os.path.join('interim','lords_count.csv')
OUT_PATH = os.path.join('interim_2','membership_2000_2025.csv')

df = pd.read_csv(IN_PATH)


df['date'] = pd.to_datetime(df['date'])
df = df[(df['date'] >= '2000-01-01') & (df['date'] <= '2025-12-31')]
df = df[['date','total']]

df.to_csv(OUT_PATH,index=False)
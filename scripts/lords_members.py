import os
import pandas as pd

OUT_PATH = os.path.join('interim','lords_count.csv')

URL = 'https://data.parliament.uk/membersdataplatform/services/mnis/HouseOverview/Lords/{}/'

dates = pd.date_range("1999-01-01", "2026-02-01", freq="MS")


summary = []

for d in dates:
    print(d.strftime("%Y-%m-%d"))
    df = pd.read_xml(URL.format(d.strftime("%Y-%m-%d")))

    summary.append({
        'date': d.strftime("%Y-%m-%d"),
        'total' : df['TotalCount'].sum(),
        'total_male' : df['MaleCount'].sum(),
        'total_female' : df['FemaleCount'].sum(),
    })


df_summary = pd.DataFrame(summary)
df_summary.to_csv(OUT_PATH,index=False)


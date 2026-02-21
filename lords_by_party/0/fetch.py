import os
import pandas as pd

OUT_PATH = os.path.join('in','lords_by_party','{}.csv')
URL = 'https://data.parliament.uk/membersdataplatform/services/mnis/HouseOverview/Lords/{}/'

dates = pd.date_range("1958-08-01", "2026-02-01", freq="MS")

for d in dates:
    d_str = d.strftime("%Y-%m-%d")
    print(d_str)
    df = pd.read_xml(URL.format(d_str))
    df.to_csv(OUT_PATH.format(d_str),index=False)
import os
import pandas as pd

IN_PATH = os.path.join('interim','lords_count.csv')
OUT_PATH = os.path.join('interim_2','{}.csv')

def filter(df,**kw):
    name,start,end,columns = kw['name'],kw['start'],kw['end'],kw['columns']
    df = df[(df['date'] >= start) & (df['date'] <= end)]
    df = df[['date'] + columns]

    df.to_csv(OUT_PATH.format(name),index=False)



plots = [
        {   'name' : 'membership_2000_2025',
            'start' : '2000-01-01',
            'end' : '2025-12-31',
            'columns' : ['total']
        },
        {   'name' : 'membership_1999_2025',
            'start' : '1999-01-01',
            'end' : '2025-12-31',
            'columns' : ['total']
        },
        {   'name' : 'membership_1960_2025',
            'start' : '1960-01-01',
            'end' : '2025-12-31',
            'columns' : ['total_male','total_female']
        },
]


main_df = pd.read_csv(IN_PATH)

#df['date'] = pd.to_datetime(df['date'])

for plot in plots:
    filter(main_df,**plot)
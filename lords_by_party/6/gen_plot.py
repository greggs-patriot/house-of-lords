import os

import pandas as pd
import matplotlib.pyplot as plt
import plot_params as ppar

#import lobals

IN_DIR= os.path.join('lords_by_party','5','{}')
OUT_PATH = os.path.join('lords_by_party','7','{}')


for in_file in os.listdir(IN_DIR.format('')):
    df = pd.read_csv(IN_DIR.format(in_file))


    df['date'] = pd.to_datetime(df['date'])

    fig, ax, ax_right = ppar.pre_settings()
    print(df.columns.to_list())
    for col in  [c for c in df.columns.to_list() if c != 'date']:
        
        ax.plot(df['date'], df[col], label='Total', color='#c00000', linewidth=1.5)

    

    ppar.post_settings(fig,ax,ax_right)

    out_file = in_file.replace('.csv','.png')
    plt.savefig(OUT_PATH.format(out_file), dpi=300, facecolor=fig.get_facecolor())


def ignore():
    ticks = pd.date_range(
        start=df['date'].min(),
        end=df['date'].max(),
        freq='5YS'   # 5-year start frequency
    )

    ax.set_xticks(ticks)
    ax.set_xticklabels([d.year for d in ticks])
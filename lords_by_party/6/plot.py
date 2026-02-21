import os

import pandas as pd
import matplotlib.pyplot as plt
import plot_params as ppar

#import lobals

IN_PATH = os.path.join('lords_by_party','5','membership_1999_2025.csv')
OUT_PATH = os.path.join('lords_by_party','7','membership_1999_2025.png')

df = pd.read_csv(IN_PATH)


df['date'] = pd.to_datetime(df['date'])

fig, ax, ax_right = ppar.pre_settings()

ax.plot(df['date'], df['total'], label='Total', color='#c00000', linewidth=1.5)

ticks = pd.date_range(
    start=df['date'].min(),
    end=df['date'].max(),
    freq='5YS'   # 5-year start frequency
)


ax.set_xticks(ticks)
ax.set_xticklabels([d.year for d in ticks])

ppar.post_settings(fig,ax,ax_right)

plt.savefig(OUT_PATH, dpi=300, facecolor=fig.get_facecolor())

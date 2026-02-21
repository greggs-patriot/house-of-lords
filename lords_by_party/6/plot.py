import os

import pandas as pd
import matplotlib.pyplot as plt
import plot_params as ppar

IN_PATH = os.path.join('interim_2','membership_2000_2025.csv')
OUT_PATH = os.path.join('out','lords_membership.png')

df = pd.read_csv(IN_PATH)


df['date'] = pd.to_datetime(df['date'])
#df = df[(df['date'] >= '2000-01-01') & (df['date'] <= '2025-12-31')]


fig, ax, ax_right = ppar.default_settings()

ax.plot(df['date'], df['total'], label='Total', color='#c00000', linewidth=1.5)
ax_right.set_ylim(ax.get_ylim())


ax.set_title('House of Lords Membership numbers', x=0.03, loc='left',fontsize=24)


ticks = pd.date_range(
    start=df['date'].min(),
    end=df['date'].max(),
    freq='5YS'   # 5-year start frequency
)

ax.set_xticks(ticks)
ax.set_xticklabels([d.year for d in ticks])


ax.tick_params(axis='x', labelsize=24)


fig.text(
    0.5, 0.01,
    "Source: UK Parliament – Members' Names Data Platform (Lords by membership type); "
    "Elections & Polling Team, Trafalgar Analytics",
    ha='center',
    va='bottom',
    fontsize=9,
)

plt.tight_layout(rect=[0, 0.025, 1, 1])
plt.savefig(OUT_PATH, dpi=300, facecolor=fig.get_facecolor())
plt.show()
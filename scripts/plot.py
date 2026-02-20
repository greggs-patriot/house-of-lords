import os

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

IN_PATH = os.path.join('interim','lords_count.csv')
OUT_PATH = os.path.join('out','lords_membership.png')

def default_settings():
    fig, ax = plt.subplots(figsize=(10, 6))
    bg_colour = '#fff9f5'
    
    fig.patch.set_facecolor(bg_colour)
    ax.set_facecolor(bg_colour)

    ax.spines['top'].set_visible(False)
    
    ax.margins(x=0.025)

    ax_right = ax.twinx()
    

    ax_right.spines['top'].set_visible(False)


    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    ax_right.spines['right'].set_linewidth(1.5)
    
    ax.tick_params(axis='y', labelsize=20)
    ax_right.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)

    return fig,ax,ax_right


df = pd.read_csv(IN_PATH)


df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')
df = df[(df['date'] >= '2000-01-01') & (df['date'] <= '2025-12-31')]


fig, ax, ax_right = default_settings()

ax.plot(df['date'], df['total'], label='Total', color='#c00000', linewidth=1.5)
ax_right.set_ylim(ax.get_ylim())


ax.set_title('House of Lords Membership numbers', x=0.03, loc='left',fontsize=24)
#ax.xaxis.set_major_locator(mdates.YearLocator(base=5))


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
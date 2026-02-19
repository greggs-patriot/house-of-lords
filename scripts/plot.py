import os

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.dates as mdates
from matplotlib import font_manager

IN_PATH = os.path.join('interim','lords_count.csv')
OUT_PATH = os.path.join('out','lords_membership.png')

# -----------------------
# Load data
# -----------------------
df = pd.read_csv(IN_PATH)

# Ensure date column is datetime
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')
df = df[(df['date'] >= '2000-01-01') & (df['date'] <= '2025-12-31')]

# -----------------------
# Styling
# -----------------------
#rcParams['font.family'] = 'Microsoft Sans Serif', 'DejaVu Sans'

rcParams['font.size'] = 20

bg_colour = '#fff9f5'

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor(bg_colour)
ax.set_facecolor(bg_colour)

# -----------------------
# Plot lines
# -----------------------
ax.plot(df['date'], df['total'], label='Total', color='#c00000', linewidth=1.5)
#ax.plot(df['date'], df['total_male'], label='Male')
#ax.plot(df['date'], df['total_female'], label='Female')

# Labels
ax.set_title('House of Lords Membership numbers', x=0.03, loc='left')
ax.xaxis.set_major_locator(mdates.YearLocator(base=5))
#ax.set_xlabel('Date')
ax.margins(x=0.025)
#ax.set_ylabel('Number of Members')

# Clean think-tank style
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#ax.legend()

ax_right = ax.twinx()
ax_right.set_ylim(ax.get_ylim())

ax.spines['top'].set_visible(False)
ax_right.spines['top'].set_visible(False)
ax.tick_params(axis='x', labelsize=24)

for spine in ax.spines.values():
    spine.set_linewidth(1.5)

for spine in ax_right.spines.values():
    spine.set_linewidth(1.5)

fig.text(
    0.5, 0.01,
    "Source: UK Parliament – Members' Names Data Platform (Lords by membership type); "
    "Elections & Polling Team, Trafalgar Analytics",
    ha='center',
    va='bottom',
    fontsize=9,
)

plt.tight_layout()
plt.savefig(OUT_PATH, dpi=300, facecolor=fig.get_facecolor())
plt.show()
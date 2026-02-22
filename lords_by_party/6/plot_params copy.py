import matplotlib as mpl
import matplotlib.pyplot as plt

BG_COLOUR = '#fff9f5'


mpl.rcParams.update({
    # Figure / axes
    'figure.figsize': (10, 6),
    'figure.facecolor': BG_COLOUR,
    'axes.facecolor': BG_COLOUR,

    # Title defaults (you can still override per-plot)
    'axes.titlesize': 24,

    # Spines / axes lines
    'axes.spines.top': False,
    'axes.linewidth': 1.5,

    # Ticks
    'xtick.labelsize': 24,
    'ytick.labelsize': 20,
    'xtick.major.width': 1.5,
    'ytick.major.width': 1.5,

    # Lines (optional)
    'lines.linewidth': 2.0,
})

def pre_settings():
    fig, ax = plt.subplots()
    ax.set_title('House of Lords Membership numbers', x=0.03, loc='left') 

    ax_right = ax.twinx()
    ax_right.spines['top'].set_visible(False) 

    
    ax_right.spines['right'].set_linewidth(mpl.rcParams['axes.linewidth'])
    return fig, ax, ax_right

def post_settings(fig: plt.Figure, ax: plt.Axes, ax_right: plt.Axes):
    ax_right.set_ylim(ax.get_ylim())
    ax.margins(x=0.025)

    fig.text(
        0.5, 0.01,
        "Source: UK Parliament – Members' Names Data Platform (Lords by membership type); "
        "Elections & Polling Team, Trafalgar Analytics",
        ha='center', va='bottom', fontsize=9,
    )
    plt.tight_layout(rect=[0, 0.025, 1, 1]) 
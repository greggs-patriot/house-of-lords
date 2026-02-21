import matplotlib.pyplot as plt


def pre_settings():
    fig, ax = plt.subplots(figsize=(10, 6))
    bg_colour = '#fff9f5'

    ax.set_title('House of Lords Membership numbers', x=0.03, loc='left',fontsize=24)
    
    fig.patch.set_facecolor(bg_colour)
    ax.set_facecolor(bg_colour)

    ax.spines['top'].set_visible(False)
    
    ax_right = ax.twinx()
    ax_right.spines['top'].set_visible(False)


    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    ax_right.spines['right'].set_linewidth(1.5)
    
    ax.tick_params(axis='y', labelsize=20)
    ax_right.tick_params(axis='y', labelsize=20)

    ax.tick_params(axis='x', labelsize=24)

    return fig,ax,ax_right

def post_settings(fig : plt.Figure,ax : plt.Axes, ax_right : plt.Axes):
    

    ax_right.set_ylim(ax.get_ylim())
    ax.margins(x=0.025)
    
    fig.text(
        0.5, 0.01,
        "Source: UK Parliament – Members' Names Data Platform (Lords by membership type); "
        "Elections & Polling Team, Trafalgar Analytics",
        ha='center',
        va='bottom',
        fontsize=9,
    )

    plt.tight_layout(rect=[0, 0.025, 1, 1])
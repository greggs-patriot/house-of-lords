import matplotlib.pyplot as plt


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
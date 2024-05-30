import matplotlib.pyplot as plt


def plot_logs(df,figsize=(12,12)):
    fig, axes = plt.subplots(1,4,figsize=figsize)

    for ax in axes:
        ax.set_ylim(df['DEPTH_MD'].max()+50, df['DEPTH_MD'].min()-150)
        ax.grid()

    axes[0].plot(df['GR'],df['DEPTH_MD'], label='GR', color='blue',lw=0.8)
    axes[0].set_xlabel('uAPI')
    axes[0].set_ylabel('Depth MD')
    ax0 = axes[0].twiny()
    ax0.plot(df['CALI'], df['DEPTH_MD'], label='CALI', color='red',lw=0.8,ls='-.')
    ax0.set_xlabel('CALI')
    axes[0].legend(loc='upper left')
    ax0.legend(loc='upper right')

    axes[1].plot(df['RMED'],df['DEPTH_MD'], label='RMED', color='blue',lw=0.8)
    axes[1].plot(df['RDEP'],df['DEPTH_MD'], label='RDEP', color='red',lw=0.8,ls='-.')
    axes[1].set_xlabel(r'$\Omega m$')
    axes[1].legend(loc='upper left')
    axes[1].set_xscale('log')

    axes[2].plot(df['DTC'],df['DEPTH_MD'], label='DTC', color='blue',lw=0.8)
    axes[2].set_xlabel(r'$\mu / s$')

    axes[3].plot(df['RHOB'],df['DEPTH_MD'], label='RHOB', color='blue',lw=0.8)
    axes[3].set_xlabel(r'g/cm$^3$')
    ax3 = axes[3].twiny()
    ax3.plot(df['NPHI'], df['DEPTH_MD'], label='NPHI', color='red',lw=0.8,ls='-.')
    ax3.set_xlabel('')
    axes[3].legend(loc='upper left')
    ax3.legend(loc='upper right')

    fig.text(x=0.48,y=0.98,s=df.WELL.unique()[0],fontsize=16)

    fig.tight_layout()

    return
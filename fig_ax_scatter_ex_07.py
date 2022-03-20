#! /usr/bin/env python3
"""
Create grid of Anscombe's quarter of scatter plots.
Use LaTeX to show equation in legend.
Label figure, axes.
Title figure, axes.
"""

import matplotlib.pyplot as plt

from numpy.polynomial import polynomial as nppoly
import datasense as ds


def main():
    metadata_dict = {
        'Creator': 'Gilles Pilon',
        'Publisher': 'Gilles Pilon',
        'Title': 'Single figure, single axes graph',
        'Keywords': ['matplotlib', 'figure', 'axes'],
        'Rights': 'Copyright 2020 Gilles Pilon'
    }
    axes_title = ['AQ1', 'AQ2', 'AQ3', 'AQ4']
    colour1, colour2 = '#0077bb', '#33bbee'
    left, right, top, bottom = 2, 20, 14, 2
    x_axis_label = 'X axis label (units)'
    y_axis_label = 'Y axis label (units)'
    fig_title = "Anscombe's Quartet"
    figsize = (12, 9)
    fig = plt.figure(figsize=figsize)
    fig.suptitle(t=fig_title, fontweight='bold')
    for index in range(1, 5):
        df = ds.read_file(file_name=f'aq{index}.csv')
        ax = fig.add_subplot(2, 2, index)
        ax.plot(
            df['x'],
            df['y'],
            marker='.',
            linestyle='',
            color=colour1
        )
        b, m = nppoly.polyfit(df['x'], df['y'], 1)
        equation = f"$y = {b:.1f} + {m:.1f}x$"
        ax.plot(df['x'], m*df['x'] + b, '-', color=colour2, label=equation)
        ax.set_ylim(
            bottom=bottom,
            top=top
        )
        ax.set_xlim(
            left=left,
            right=right
        )
        ax.set_title(label=f"{axes_title[index-1]}", fontweight="bold")
        ax.set_ylabel(ylabel=y_axis_label, fontweight="bold")
        ax.set_xlabel(xlabel=x_axis_label, fontweight="bold")
        # ax.text(
        #     x=ax.get_xlim()[0] + .25,
        #     y=ax.get_ylim()[1],
        #     s=f"$y = {b:.1f} + {m:.1f}x$\n",
        #     fontsize=8
        # )
        # ax.text(
        #     x=0,
        #     y=1,
        #     s=f"$y = {b:.1f} + {m:.1f}x$\n",
        #     fontsize=8,
        #     transform=ax.transAxes
        # )
        ax.legend(frameon=False)
        ds.despine(ax=ax)
    plt.tight_layout(pad=3)
    fig.savefig(
        fname='fig_ax_scatter_ex_07.svg',
        format='svg',
        metadata=metadata_dict
    )


if __name__ == '__main__':
    main()

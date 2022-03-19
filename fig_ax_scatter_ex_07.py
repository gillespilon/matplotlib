#! /usr/bin/env python3
"""
Create grid of Anscombe's quarter of scatter plots.
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
        ax.plot(df['x'], m*df['x'] + b, '-', color=colour2)
        ax.set_ylim(
            bottom=2,
            top=14
        )
        ax.set_xlim(
            left=2,
            right=20
        )
        ax.set_title(
            label=f"{axes_title[index-1]}\n"
            f"$y = {b:.1f} + {m:.1f}x$"
        )
        ax.set_ylabel(ylabel=y_axis_label)
        ax.set_xlabel(xlabel=x_axis_label)
        ds.despine(ax=ax)
    plt.tight_layout(pad=3)
    fig.savefig(
        fname='fig_ax_scatter_ex_07.svg',
        format='svg',
        metadata=metadata_dict
    )


if __name__ == '__main__':
    main()

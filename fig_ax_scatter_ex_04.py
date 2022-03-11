#! /usr/bin/env python3
"""
Create side-by-side scatter plots.
Add labels, titles to Figure, Axes.
Add lines for averages.
"""

import matplotlib.pyplot as plt
import pandas as pd


def main():
    data = {
        'x': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        'y': [
            32, 37, 35, 28, 41, 44, 35, 31, 34, 38, 42, 36, 31, 30, 31, 34,
            36, 29, 32, 31
        ]
    }
    # apply style sheet
    # https://matplotlib.org/stable/gallery/style_sheets/\
    #    style_sheets_reference.html
    # print(plt.style.available)
    plt.style.use('fivethirtyeight')
    # plt.style.use('ggplot')
    # create DataFrames
    df = pd.DataFrame(data=data)
    sample_one = df[df['x'] == 1]
    sample_two = df[df['x'] == 2]
    # create Figure, Axes objects
    fig, (ax1, ax2) = plt.subplots(
        nrows=1, ncols=2, sharex=True, sharey=True, layout='tight'
    )
    # remove two spines
    for spine in 'right', 'top':
        ax1.spines[spine].set_visible(False)
        ax2.spines[spine].set_visible(False)
    # add Figure title
    fig.suptitle(
        t='Scatter plots for two samples', fontweight='bold', fontsize=14
    )
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    ax1.plot(sample_one['y'], marker='.', markersize=8, linestyle='None',)
    # add Axes title
    ax1.set_title(label='Sample one', fontweight='bold', fontsize=12)
    # add y axis title
    ax1.set_ylabel(ylabel='y', fontweight='bold')
    # add x axis title
    ax1.set_xlabel(
        xlabel='Sample no. within sample one', fontweight='bold', fontsize=10
    )
    # add average line
    ax1.axhline(
        y=sample_one['y'].mean(), xmin=0.05, xmax=0.95, color='#ff0000',
        linestyle='-', linewidth=1, label='ave'
    )
    # add legend to ax1
    # ax1.legend(['one', 'ave'])
    ax1.legend(frameon=False, loc='best')
    ax2.plot(sample_two['y'], marker='.', markersize=8, linestyle='None')
    ax2.set_xlabel(
        xlabel='Sample no. within sample two', fontweight='bold', fontsize=10
    )
    ax2.set_title(label='Sample two', fontweight='bold', fontsize=12)
    # add average line
    ax2.axhline(
        y=sample_two['y'].mean(), xmin=0.05, xmax=0.95, color='#ff0000',
        linestyle='-', linewidth=1, label='ave'
    )
    # add legend to ax2
    ax2.legend(frameon=False, loc='best')
    # save image as file
    fig.savefig(fname="fig_ax_scatter_ex_04.svg", format="svg")


if __name__ == '__main__':
    main()


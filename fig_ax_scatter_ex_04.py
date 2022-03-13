#! /usr/bin/env python3
"""
Create side-by-side scatter plots.
Add labels, titles to Figure, Axes.
Add lines for averages.
"""

from matplotlib.ticker import MultipleLocator
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
    # https://matplotlib.org/stable/api/figure_api.html
    # class matplotlib.figure.Figure
    # https://matplotlib.org/stable/api/axes_api.html
    # class matplotlib.axes.Axes
    # pydoc matplotlib.pyplot.subplots
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True)
    # remove two spines
    for spine in 'right', 'top':
        ax1.spines[spine].set_visible(False)
        ax2.spines[spine].set_visible(False)
    # add Figure title
    # https://matplotlib.org/stable/api/figure_api.html
    # pydoc matplotlib.figure.Figure.suptitle
    fig.suptitle(
        t='Scatter plots for two samples', fontweight='bold', fontsize=14
    )
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    # pydoc matplotlib.axes.Axes.plot
    ax1.plot(sample_one['y'], marker='.', markersize=8, linestyle='None')
    # add Axes title
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_title.html
    # pydoc matplotlib.axes.Axes.set_title
    ax1.set_title(label='Sample one', fontweight='bold', fontsize=12)
    # add y axis label
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_ylabel.html
    # pydoc matplotlib.axes.Axes.set_ylabel
    ax1.set_ylabel(ylabel='y', fontweight='bold')
    # add x axis label
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_xlabel.html
    # pydoc matplotlib.axes.Axes.set_xlabel
    ax1.set_xlabel(
        xlabel='Sample no. within sample one', fontweight='bold', fontsize=10
    )
    # add average line
    ax1.axhline(
        y=sample_one['y'].mean(), xmin=0.05, xmax=0.95, color='#ff0000',
        linestyle='-', linewidth=1, label='ave'
    )
    # set tick spacing, argument is int or float
    ax1.xaxis.set_major_locator(locator=MultipleLocator(base=5))
    ax1.yaxis.set_major_locator(locator=MultipleLocator(base=2))
    # to set the format of the tick labels, use set_major_formatter
    # add legend to ax1
    # ax1.legend(['one', 'ave'])
    ax1.legend(frameon=False, loc='best')
    ax2.plot(sample_two['y'], marker='.', markersize=8, linestyle='None')
    # add x axis label
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_xlabel.html
    # pydoc matplotlib.axes.Axes.set_xlabel
    ax2.set_xlabel(
        xlabel='Sample no. within sample two', fontweight='bold', fontsize=10
    )
    # add Axes title
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_title.html
    # pydoc matplotlib.axes.Axes.set_title
    ax2.set_title(label='Sample two', fontweight='bold', fontsize=12)
    # add average line
    ax2.axhline(
        y=sample_two['y'].mean(), xmin=0.05, xmax=0.95, color='#ff0000',
        linestyle='-', linewidth=1, label='ave'
    )
    # add legend to ax2
    ax2.legend(frameon=False, loc='best')
    # adjust the padding between and around subplots
    # https://matplotlib.org/stable/api/figure_api.html
    # pydoc matplotlib.figure.Figure.tight_layout
    fig.tight_layout()
    # save image as file
    # https://matplotlib.org/stable/api/figure_api.html
    # pydoc matplotlib.figure.Figure.savefig
    # save image as file
    fig.savefig(fname="fig_ax_scatter_ex_04.svg", format="svg")


if __name__ == '__main__':
    main()

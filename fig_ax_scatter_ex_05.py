#! /usr/bin/env python3
"""
Create a simple scatter plot.
Format the y axis as floats.
Format the x axis as dates and rotate.
"""

from matplotlib.ticker import FormatStrFormatter
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd


def main():
    data = {
        'x': [
            '2022-03-01', '2022-03-02', '2022-03-03', '2022-03-04',
            '2022-03-05', '2022-03-06', '2022-03-07', '2022-03-08',
            '2022-03-09', '2022-03-10', '2022-03-11', '2022-03-12',
            '2022-03-13'
        ],
        'y': [32, 37, 35, 28, 41, 44, 35, 31, 34, 38, 42, 36, 31]
    }
    # create DataFrames
    df = pd.DataFrame(data=data).astype(
        dtype={'x': 'datetime64[ns]', 'y': 'int64'}
    )
    # create Figure, Axes objects
    # https://matplotlib.org/stable/api/figure_api.html
    # class matplotlib.figure.Figure
    # https://matplotlib.org/stable/api/axes_api.html
    # class matplotlib.axes.Axes
    # pydoc matplotlib.pyplot.subplots
    fig, ax = plt.subplots(nrows=1, ncols=1)
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    # pydoc matplotlib.axes.Axes.plot
    ax.plot(df['x'], df['y'], linestyle='None', marker='.', markersize=8)
    # add Axes title
    ax.set_title(label='Y vs X scatter plot', fontweight='bold', fontsize=12)
    # add y axis title
    ax.set_ylabel(ylabel='y', fontweight='bold')
    # add x axis title
    ax.set_xlabel(
        xlabel='Date (yyyy-mm-dd)', fontweight='bold', fontsize=10
    )
    # format x axis tick labels
    # "label" is of type Text, which has a method "set"
    # https://matplotlib.org/stable/api/text_api.html
    ax.xaxis.set_major_formatter(formatter=mdates.DateFormatter('%Y-%m-%d'))
    for label in ax.get_xticklabels(which='major'):
        label.set(rotation=30, horizontalalignment='right')
    # format y axis tick labels
    ax.yaxis.set_major_formatter(formatter=FormatStrFormatter('%.1f'))
    # save image as file
    fig.tight_layout()
    fig.savefig(fname="fig_ax_scatter_ex_05.svg", format="svg")


if __name__ == '__main__':
    main()

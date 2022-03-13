#! /usr/bin/env python3
"""
Create two scatter plots with different y axes.
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
        'y1': [32, 37, 35, 28, 41, 44, 35, 31, 34, 38, 42, 36, 31],
        'y2': [40, 46, 43, 38, 48, 53, 45, 38, 44, 45, 51, 43, 41]
    }
    color_y1 = '#0000ff'
    color_y2 = '#ff0000'
    # create DataFrames
    df = pd.DataFrame(data=data).astype(
        dtype={'x': 'datetime64[ns]', 'y1': 'int64', 'y2': 'int64'}
    )
    # create Figure, Axes objects
    # https://matplotlib.org/stable/api/figure_api.html
    # class matplotlib.figure.Figure
    # https://matplotlib.org/stable/api/axes_api.html
    # class matplotlib.axes.Axes
    # pydoc matplotlib.pyplot.subplots
    fig, ax1 = plt.subplots(nrows=1, ncols=1)
    ax2 = ax1.twinx()
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    # pydoc matplotlib.axes.Axes.plot
    ax1.plot(
        df['x'], df['y1'], linestyle='None', marker='.', markersize=8,
        color=color_y1
    )
    # add Axes title
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_title.html
    # pydoc matplotlib.axes.Axes.set_title
    ax1.set_title(
        label='Y1, Y2 vs X scatter plot', fontweight='bold', fontsize=12
    )
    # add y axis label
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_ylabel.html
    # pydoc matplotlib.axes.Axes.set_ylabel
    ax1.set_ylabel(ylabel='y1', fontweight='bold', color=color_y1)
    ax1.tick_params(axis='y', colors=color_y1)
    # add x axis label
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_xlabel.html
    # pydoc matplotlib.axes.Axes.set_xlabel
    ax1.set_xlabel(
        xlabel='Date (yyyy-mm-dd)', fontweight='bold', fontsize=10
    )
    # format x axis tick labels
    # "label" is of type Text, which has a method "set"
    # https://matplotlib.org/stable/api/text_api.html
    ax1.xaxis.set_major_formatter(formatter=mdates.DateFormatter('%Y-%m-%d'))
    for label in ax1.get_xticklabels(which='major'):
        label.set(rotation=30, horizontalalignment='right')
    # format y axis tick labels
    ax1.yaxis.set_major_formatter(formatter=FormatStrFormatter('%.1f'))
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    # pydoc matplotlib.axes.Axes.plot
    ax2.plot(
        df['x'], df['y2'], linestyle='None', marker='+', markersize=8,
        color=color_y2
    )
    # add y axis label
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_ylabel.html
    # pydoc matplotlib.axes.Axes.set_ylabel
    ax2.set_ylabel(ylabel='y2', fontweight='bold', color=color_y2)
    ax2.tick_params(axis='y', colors=color_y2)
    # change color of axis spine
    for ax, spine, color in zip(
        [ax1, ax1, ax2, ax2],
        ['left', 'right', 'left', 'right'],
        [color_y1, color_y2, color_y1, color_y2]
    ):
        ax.spines[spine].set_color(c=color)
    for label in ax2.get_yticklabels():
        label.set_color(color_y2)
    # adjust the padding between and around subplots
    # https://matplotlib.org/stable/api/figure_api.html
    # pydoc matplotlib.figure.Figure.tight_layout
    fig.tight_layout()
    # save image as file
    # https://matplotlib.org/stable/api/figure_api.html
    # pydoc matplotlib.figure.Figure.savefig
    # save image as file
    fig.savefig(fname="fig_ax_scatter_ex_06.svg", format="svg")


if __name__ == '__main__':
    main()

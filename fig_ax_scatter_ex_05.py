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
    spines_to_remove = ['top', 'right']
    # https://matplotlib.org/stable/gallery/color/color_demo.html
    # https://matplotlib.org/stable/tutorials/colors/colors.html
    colour_one = '#0077bb'
    # create DataFrames
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
    # pydoc pandas.DataFrame
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
    # remove two spines
    # https://matplotlib.org/stable/api/spines_api.html
    # pydoc matplotlib.spines
    ax.spines[spines_to_remove].set_visible(False)
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    # pydoc matplotlib.axes.Axes.plot
    ax.plot(
        df['x'], df['y'], linestyle='None', marker='.', markersize=8,
        color=colour_one
    )
    # add Axes title
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_title.html
    # pydoc matplotlib.axes.Axes.set_title
    ax.set_title(label='Y vs X scatter plot', fontweight='bold', fontsize=12)
    # add y axis label
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_ylabel.html
    # pydoc matplotlib.axes.Axes.set_ylabel
    ax.set_ylabel(ylabel='y', fontweight='bold')
    # add x axis label
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_xlabel.html
    # pydoc matplotlib.axes.Axes.set_xlabel
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
    # adjust the padding between and around subplots
    # https://matplotlib.org/stable/api/figure_api.html
    # pydoc matplotlib.figure.Figure.tight_layout
    fig.tight_layout()
    # save image as file
    # https://matplotlib.org/stable/api/figure_api.html
    # pydoc matplotlib.figure.Figure.savefig
    # save image as file
    fig.savefig(fname="fig_ax_scatter_ex_05.svg", format="svg")


if __name__ == '__main__':
    main()

#! /usr/bin/env python3
"""
Create side-by-side scatter plots.
Add labels, titles to Figure, Axes.
Add lines for averages.
Add legend.
"""

from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import datasense as ds
import pandas as pd


def main():
    data = {
        'x': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        'y': [
            32, 37, 35, 28, 41, 44, 35, 31, 34, 38, 42, 36, 31, 30, 31, 34,
            36, 29, 32, 31
        ]
    }
    ds.style_graph()
    # https://matplotlib.org/stable/gallery/color/color_demo.html
    # https://matplotlib.org/stable/tutorials/colors/colors.html
    colour_one, colour_two = '#0077bb', '#ee7733'
    # apply style sheet
    # https://matplotlib.org/stable/api/style_api.html
    # https://matplotlib.org/stable/gallery/style_sheets/
    #    style_sheets_reference.html
    # pydoc matplotlib.style
    plt.style.use('fivethirtyeight')
    # plt.style.use('ggplot')
    # create DataFrames
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
    # pydoc pandas.DataFrame
    df = pd.DataFrame(data=data)
    sample_one = df[df['x'] == 1]
    sample_two = df[df['x'] == 2]
    # create Figure, Axes objects
    # https://matplotlib.org/stable/api/figure_api.html
    # class matplotlib.figure.Figure
    # https://matplotlib.org/stable/api/axes_api.html
    # class matplotlib.axes.Axes
    # https://matplotlib.org/stable/api/
    #     figure_api.html#matplotlib.figure.Figure.subplots
    # pydoc matplotlib.figure.Figure.subplots
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True)
    # add Figure title
    # https://matplotlib.org/stable/api/figure_api.html#suptitle
    # pydoc matplotlib.figure.Figure.suptitle
    fig.suptitle(t='Scatter plots for two samples')
    # create scatter plot
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    # pydoc matplotlib.axes.Axes.plot
    ax1.plot(
        sample_one['y'], marker='.', markersize=8, linestyle='None',
        color=colour_one
    )
    # add Axes title
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_title.html
    # pydoc matplotlib.axes.Axes.set_title
    ax1.set_title(label='Sample one')
    # add y axis label
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_ylabel.html
    # pydoc matplotlib.axes.Axes.set_ylabel
    ax1.set_ylabel(ylabel='y')
    # add x axis label
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_xlabel.html
    # pydoc matplotlib.axes.Axes.set_xlabel
    ax1.set_xlabel(xlabel='Sample item')
    # add average line
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.axhline.html
    # pydoc matplotlib.axes.Axes.axhline
    ax1.axhline(
        y=sample_one['y'].mean(), xmin=0.05, xmax=0.95, color=colour_one,
        linestyle='-', linewidth=1, label='ave'
    )
    # set tick spacing, argument is int or float
    # https://matplotlib.org/stable/api/axes_api.html
    # class matplotlib.axes.Axes
    # pydoc matplotlib.axes.Axes
    # use ax.xaxis and ax.yaxis attributes
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axis.Axis.set_major_locator.html
    # pydoc matplotlib.axis.XAxis.set_major_locator
    # to set the format of the tick labels, use set_major_formatter
    ax1.xaxis.set_major_locator(locator=MultipleLocator(base=5))
    ax1.yaxis.set_major_locator(locator=MultipleLocator(base=2))
    # add legend to ax1
    # matplotlib.legend](https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.legend.html
    ax1.legend(frameon=False, loc='best')
    # create scatter plot
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    # pydoc matplotlib.axes.Axes.plot
    ax2.plot(
        sample_two['y'], marker='.', markersize=8, linestyle='None',
        color=colour_two
    )
    # add x axis label
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_xlabel.html
    # pydoc matplotlib.axes.Axes.set_xlabel
    ax2.set_xlabel(xlabel='Sample item')
    # add Axes title
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.set_title.html
    # pydoc matplotlib.axes.Axes.set_title
    ax2.set_title(label='Sample two')
    # add average line
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.axhline.html
    # pydoc matplotlib.axes.Axes.axhline
    ax2.axhline(
        y=sample_two['y'].mean(), xmin=0.05, xmax=0.95, color=colour_two,
        linestyle='-', linewidth=1, label='ave'
    )
    # add legend to ax2
    # https://matplotlib.org/stable/api/_as_gen/
    #     matplotlib.axes.Axes.legend.html
    # pydoc matplotlib.axes.Axes.legend
    ax2.legend(frameon=False, loc='best')
    # adjust the padding between and around subplots
    # https://matplotlib.org/stable/api/
    #     figure_api.html#matplotlib.figure.Figure.tight_layout
    # pydoc matplotlib.figure.Figure.tight_layout
    fig.tight_layout()
    # save image as file
    # https://matplotlib.org/stable/api/figure_api.html
    # pydoc matplotlib.figure.Figure.savefig
    fig.savefig(fname="fig_ax_scatter_ex_04.svg", format="svg")


if __name__ == '__main__':
    main()

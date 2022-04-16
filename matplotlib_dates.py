#! /usr/bin/env python3
"""
Explore plotting with matplotlib dates

time -f '%e' ./matplotlib_dates.py
./matplotlib_dates.py

References
https://docs.python.org/3/library/datetime.html#module-datetime
https://matplotlib.org/api/dates_api.html#matplotlib-date-format
"""

# TODO:
# fix two subplot function to accept four series instead of two dfs
# fix one subplot function to accept two series insteead of one df
# change call to graph functions so that they return ax and then add info

from typing import List, Optional, Tuple

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.axes as axes
from datetime import datetime
import datasense as ds
import pandas as pd


def main():
    output_url = 'matplotlib_dates.html'
    header_title = 'matplotlib_dates'
    header_id = 'matplotlib-dates'
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    figsize = (8, 6)
    colour1 = '#0077bb'
    pd.options.display.max_columns = 600
    pd.options.display.max_rows = 600
    figure_title = 'Figure title'
    axis_title = 'Axis title'
    abscissa_label = 'abscissa'
    ordinate_label = 'ordinate'
    column_abscissa_datefloat_one = 'datefloats_one'
    column_abscissa_datetime_one = 'datetimes_one'
    column_abscissa_datefloat_two = 'datefloats_two'
    column_abscissa_datetime_two = 'datetimes_two'
    column_abscissa_one = 'abscissa_one'
    column_abscissa_two = 'abscissa_two'
    column_ordinate_one = 'ordinate_one'
    column_ordinate_two = 'ordinate_two'
    raw = {
        column_abscissa_one: [
            '2018-07-31', '2018-08-04', '2018-08-06', '2018-08-11',
            '2018-08-12', '2018-08-15', '2018-08-16', '2018-08-17',
            '2018-08-18', '2018-08-25', '2018-09-15'
        ],
        column_abscissa_two: [
            '2019-07-11', '2019-07-14', '2019-07-16', '2019-07-21',
            '2019-08-12', '2019-08-13', '2019-08-16', '2019-08-18',
            '2019-08-21', '2019-08-25', '2019-09-05'
        ],
        column_ordinate_one: [10, 15, 30, 35, 40, 45, 40, 30, 35, 50, 75],
        column_ordinate_two: [20, 35, 20, 15, 30, 45, 50, 40, 45, 50, 65]
    }
    data = pd.DataFrame(data=raw)
    print(
        f'DataFrame:\n'
        f'{data}\n'
    )
    # Creates a list of datetime objects
    data[column_abscissa_datetime_one] =\
        str_to_datetime(data[column_abscissa_one])
    data[column_abscissa_datefloat_one] =\
        [mdates.date2num(date)
         for date in data[column_abscissa_datetime_one]]
    data[column_abscissa_datetime_two] =\
        str_to_datetime(data[column_abscissa_two])
    data[column_abscissa_datefloat_two] =\
        [mdates.date2num(date)
         for date in data[column_abscissa_datetime_two]]
    print(
        f'DataFrame:\n'
        f'{data}\n'
    )
    print(
        f'Column data types\n'
        f'abscissa_one  : {data[column_abscissa_one].dtype}\n'
        f'abscissa_two  : {data[column_abscissa_two].dtype}\n'
        f'ordinate_one  : {data[column_ordinate_one].dtype}\n'
        f'ordinate_two  : {data[column_ordinate_two].dtype}\n'
        f'datetimes_one : {data[column_abscissa_datetime_one].dtype}\n'
        f'dates_one     : {data[column_abscissa_datefloat_one].dtype}\n'
        f'datetimes_two : {data[column_abscissa_datetime_two].dtype}\n'
        f'dates_two     : {data[column_abscissa_datefloat_two].dtype}\n'
    )
    # plot_line_two_subplots(
    #     data, column_abscissa, column_ordinate_one,
    #     file_name_graph, figsize, figure_title, axis_title,
    #     abscissa_label, ordinate_label
    # )
    # Test line plot x y, smoothing None
    fig, ax = ds.plot_line_x_y(
        X=data[column_abscissa_datetime_one],
        y=data[column_ordinate_one],
        figsize=figsize
    )
    plot_pretty(
        fig=fig,
        ax=ax,
        file_name_graph='matplotlib_dates_line_plot.svg',
        abscissa_label=abscissa_label,
        ordinate_label=ordinate_label
    )
    # Test scatter plot x y, smoothing None
    fig, ax = ds.plot_scatter_x_y(
        X=data[column_abscissa_datetime_one],
        y=data[column_ordinate_one],
        figsize=figsize
    )
    plot_pretty(
        fig,
        ax,
        'matplotlib_dates_scatter_plot.svg',
        abscissa_label=abscissa_label,
        ordinate_label=ordinate_label,
        figure_title=figure_title,
        axis_title=axis_title
    )
    # Test lineleft lineright plot x y1, y2, smoothing None
    fig, ax1, ax2 = ds.plot_lineleft_lineright_x_y1_y2(
        X=data[column_abscissa_datetime_one],
        y1=data[column_ordinate_one],
        y2=data[column_ordinate_two],
        figsize=figsize
    )
    plot_pretty(
        fig,
        ax1,
        file_name_graph='matplotlib_dates_lineleft_lineright_plot.svg',
        abscissa_label=abscissa_label,
        ordinate_label=ordinate_label,
        figure_title=figure_title,
        axis_title=axis_title
    )
    # Test lineleft lineright plot x y1, y2, smoothing Yes
    fig, ax1, ax2 = ds.plot_lineleft_lineright_x_y1_y2(
        X=data[column_abscissa_datetime_one],
        y1=data[column_ordinate_one],
        y2=data[column_ordinate_two],
        smoothing='natural_cubic_spline',
        number_knots=5,
        figsize=figsize
    )
    plot_pretty(
        fig,
        ax1,
        'matplotlib_dates_lineleft_lineright_plot_smoothing.svg',
        abscissa_label,
        ordinate_label,
        figure_title=figure_title,
        axis_title=axis_title,
    )
    # Test line plot x y, smoothing = 'natural_cubic_spline'
    fig, ax = ds.plot_line_x_y(
        data[column_abscissa_datetime_one],
        data[column_ordinate_one],
        smoothing='natural_cubic_spline',
        number_knots=5,
        figsize=figsize
    )
    plot_pretty(
        fig,
        ax,
        'matplotlib_dates_line_plot_smoothing.svg',
        abscissa_label,
        ordinate_label,
        axis_title=axis_title,
        figure_title=None,
    )
    # Test scatter plot x y, smoothing = 'natural_cubic_spline'
    fig, ax = ds.plot_scatter_x_y(
        X=data[column_abscissa_datetime_one],
        y=data[column_ordinate_one],
        figsize=figsize,
        smoothing='natural_cubic_spline',
        number_knots=5
    )
    plot_pretty(
        fig,
        ax,
        'matplotlib_dates_scatter_plot_smoothing.svg',
        abscissa_label,
        ordinate_label,
        figure_title=figure_title,
    )
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


def plot_pretty(
    fig: plt.figure,
    ax: axes.Axes,
    file_name_graph: str = None,
    abscissa_label: str = None,
    ordinate_label: str = None,
    *,
    figure_title: Optional[str] = None,
    axis_title: str = None
) -> None:
    ds.despine(ax)
    fig.suptitle(t=figure_title, fontweight='bold', fontsize=16)
    ax.set_title(label=axis_title, fontweight='bold')
    ax.set_xlabel(xlabel=abscissa_label, fontweight='bold')
    ax.set_ylabel(ylabel=ordinate_label, fontweight='bold')
    fig.savefig(fname=file_name_graph, format='svg')
    ds.html_figure(file_name=file_name_graph)


def plot_line_two_subplots(
    dataframe: pd.DataFrame,
    columnx: str,
    columny: str,
    filenamegraph: str,
    figurewidthheight: Tuple[float],
    figuretitle: str,
    axistitle: str,
    xlabel: str,
    ylabel: str
) -> None:
    fig = plt.figure(figsize=figurewidthheight)
    loc = mdates.AutoDateLocator()
    fmt = mdates.AutoDateFormatter(loc)
    ax1 = fig.add_subplot(121)
    ax1.xaxis.set_major_locator(locator=loc)
    ax1.xaxis.set_major_formatter(formatter=fmt)
    fig.autofmt_xdate()
    ax1.plot(
        dataframe[columnx],
        dataframe[columny],
        color=colour1
    )
    ds.despine(ax1)
    fig.suptitle(
        t=figuretitle,
        fontweight='bold',
        fontsize=16
    )
    ax1.set_title(
        label=axistitle,
        fontweight='bold'
    )
    ax1.set_xlabel(
        xlabel=xlabel,
        fontweight='bold'
    )
    ax1.set_ylabel(
        ylabel=ylabel,
        fontweight='bold'
    )
    ax2 = fig.add_subplot(122)
    ax2.xaxis.set_major_locator(locator=loc)
    ax2.xaxis.set_major_formatter(formatter=fmt)
    fig.autofmt_xdate()
    ax2.plot(
        dataframe[columnx],
        dataframe[columny],
        color=colour1
    )
    ds.despine(ax2)
    ax2.set_title(
        label=axistitle,
        fontweight='bold'
    )
    ax2.set_xlabel(
        xlabel=xlabel,
        fontweight='bold'
    )
    ax2.set_ylabel(
        ylabel=ylabel,
        fontweight='bold'
    )
    fig.savefig(
        fname=filenamegraph,
        format='svg'
    )


def str_to_datetime(strings: List[str]) -> List[datetime]:
    '''
    Convert a list of 'YYYY-MM-DD' strings to a list of datetime objects.
    '''
    dates = []
    for date in strings:
        y, m, d = (int(x) for x in date.split('-'))
        date = datetime(y, m, d)
        dates.append(date)
    return dates


if __name__ == '__main__':
    main()

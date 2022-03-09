#! /usr/bin/env python3
"""
Explore plotting with matplotlib dates

time -f '%e' ./matplotlib_dates.py
./matplotlib_dates.py

References
https://docs.python.org/3/library/datetime.html#module-datetime
https://matplotlib.org/api/dates_api.html#matplotlib-date-format
"""

from numpy.polynomial import polynomial as nppoly
import matplotlib.pyplot as plt
import datasense as ds
import pandas as pd


def main():
    output_url = 'matplotlib_figure_axes.html'
    header_title = 'matplotlib_figure_axes'
    header_id = 'matplotlib-figure-axes'
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    figsize = (8, 6)
    metadata_dict = {
        'Creator': 'Gilles Pilon',
        'Publisher': 'Gilles Pilon',
        'Title': 'Single figure, single axes graph',
        'Keywords': ['matplotlib', 'figure', 'axes'],
        'Rights': 'Copyright 2020 Gilles Pilon'
    }
    colour1 = '#0077bb'
    colour2 = '#33bbee'
    colour3 = '#cc3311'
    colour4 = '#009988'
    df = ds.read_file(
        file_name='weight.csv',
        parse_dates=['Date']
    )
    # Single figure, single axes
    fig_title = 'Figure title'
    axes_title = 'Axes title'
    x_axis_label = 'X axis label (units)'
    y_axis_label = 'Y axis label (units)'
    fig, ax = ds.plot_line_x_y(
        X=df['Date'],
        y=df['Steps'],
        figsize=figsize
    )
    ax.axhline(
        y=df['Steps'].median(),
        xmin=0.05,
        xmax=0.95,
        color=colour2
    )
    middle_titles = (fig.subplotpars.left + fig.subplotpars.right) / 2
    fig.suptitle(
        t=fig_title,
        x=middle_titles,
        horizontalalignment='center',
        verticalalignment='top',
        fontsize=15,
        fontweight='bold'
    )
    ax.set_ylabel(
        ylabel=y_axis_label,
        loc='center',
        fontsize=12,
        fontweight='semibold'
    )
    ax.set_xlabel(
        xlabel=x_axis_label,
        loc='center',
        fontsize=12,
        fontweight='semibold'
    )
    ax.set_title(
        label=axes_title,
        loc='center',
        horizontalalignment='center',
        verticalalignment='top',
        fontsize=12,
        fontweight='semibold'
    )
    ds.format_dates(
        fig=fig,
        ax=ax
    )
    ds.despine(ax)
    fig.savefig(
        fname='single_figure_single_axes.svg',
        format='svg',
        metadata=metadata_dict
    )
    ds.html_figure(file_name='single_figure_single_axes.svg')
    # Single figure, single axes, left y axis, right y axis
    fig_title = 'Figure title'
    axes_title = 'Axes title'
    x_axis_label = 'X axis label (units)'
    left_y_axis_label = 'Left vertical axis (units)'
    right_y_axis_label = 'Right vertical axis (units)'
    fig, ax1, ax2 = ds.plot_scatterleft_scatterright_x_y1_y2(
        X=df['Date'],
        y1=df['Actual'],
        y2=df['Steps'],
        figsize=figsize,
        linestyle2='-'
    )
    middle_titles = (fig.subplotpars.left + fig.subplotpars.right) / 2
    fig.suptitle(
        t=fig_title,
        x=middle_titles,
        horizontalalignment='center',
        verticalalignment='top',
        fontsize=15,
        fontweight='bold'
    )
    ax1.set_title(
        label=axes_title,
        fontweight='bold'
    )
    ax1.set_ylabel(
        ylabel=left_y_axis_label,
        fontweight='bold'
    )
    ax1.set_xlabel(
        xlabel=x_axis_label,
        fontweight='bold'
    )
    ax2.set_ylabel(
        ylabel=right_y_axis_label,
        fontweight='bold'
    )
    ds.format_dates(
        fig=fig,
        ax=ax1
    )
    fig.savefig(
        fname='single_figure_single_axes_left_y_right_y.svg',
        bbox_inches='tight',
        format='svg',
        metadata=metadata_dict
    )
    ds.html_figure(file_name='single_figure_single_axes_left_y_right_y.svg')
    # Single figure, two axes
    axes_title = ['Axes Title I', 'Axes Title II']
    fig = plt.figure(figsize=figsize)
    fig.suptitle(
        t=fig_title,
        fontweight='bold'
    )
    for item in range(1, 3):
        ax = fig.add_subplot(1, 2, item)
        ax.plot(
            df['Date'],
            df['Steps'],
            marker='o',
            linestyle='-',
            color=colour4
        )
        ax.set_title(label=axes_title[item-1])
        ax.set_ylabel(ylabel=y_axis_label)
        ax.set_xlabel(xlabel=x_axis_label)
        ds.format_dates(
            fig=fig,
            ax=ax
        )
        ds.despine(ax)
    plt.tight_layout(pad=3)
    fig.savefig(
        fname='single_figure_two_axes.svg',
        format='svg',
        metadata=metadata_dict
    )
    ds.html_figure(file_name='single_figure_two_axes.svg')
    # Single figure, four axes
    axes_title = ['AQ1', 'AQ2', 'AQ3', 'AQ4']
    fig = plt.figure(figsize=figsize)
    fig_title = "Anscombe's Quartet"
    fig.suptitle(
        t=fig_title,
        fontweight='bold'
    )
    for item in range(1, 5):
        df = ds.read_file(file_name=f'aq{item}.csv')
        ax = fig.add_subplot(2, 2, item)
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
        ax.set_title(label=axes_title[item-1])
        ax.set_ylabel(ylabel=y_axis_label)
        ax.set_xlabel(xlabel=x_axis_label)
        ds.despine(ax)
    plt.tight_layout(pad=3)
    fig.savefig(
        fname='single_figure_four_axes.svg',
        format='svg',
        metadata=metadata_dict
    )
    ds.html_figure(file_name='single_figure_four_axes.svg')
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == '__main__':
    main()

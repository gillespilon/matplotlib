#! /usr/bin/env python3
"""
Create grid of Anscombe's quarter of scatter plots.
Use LaTeX to show equation in legend.
Label figure, axes.
Title figure, axes.
"""

import matplotlib.pyplot as plt
from typing import Tuple

from numpy.polynomial import polynomial as nppoly
import datasense as ds
import pandas as pd


def main():
    metadata_dict = {
        'Creator': 'Gilles Pilon',
        'Publisher': 'Gilles Pilon',
        'Title': 'Single figure, single axes graph',
        'Keywords': ['matplotlib', 'figure', 'axes'],
        'Rights': 'Copyright 2020 Gilles Pilon'
    }
    axes_title = ["Data set 1", "Data set 2", "Data set 3", "Data set 4"]
    colour1, colour2 = '#0077bb', '#33bbee'
    left, right, top, bottom = 2, 20, 14, 2
    x_axis_label = 'X axis label (units)'
    y_axis_label = 'Y axis label (units)'
    fig_title = "Anscombe's Quartet"
    figsize = (12, 9)
    # create DataFrames
    df1, df2, df3, df4 = create_dataframe()
    # create fig to hold four Axes
    fig = plt.figure(figsize=figsize)
    fig.suptitle(t=fig_title, fontweight='bold')
    # create four Axes, scatter plots, regression lines
    for index in range(1, 5):
        df = eval(f"df{index}")
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
        ax.legend(frameon=False)
        ds.despine(ax=ax)
    plt.tight_layout(pad=3)
    fig.savefig(
        fname='fig_ax_scatter_ex_07.svg',
        format='svg',
        metadata=metadata_dict
    )


def create_dataframe() -> Tuple[pd.DataFrame]:
    """
    Load data into separate dataframes.
    """
    data_aq1 = {
        "x": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        "y": [
            8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68
        ],
    }
    data_aq2 = {
        "x": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        "y": [9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74],
    }
    data_aq3 = {
        "x": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        "y": [
            7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73
        ],
    }
    data_aq4 = {
        "x": [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
        "y": [
            6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89
        ],
    }
    df1 = pd.DataFrame(data=data_aq1)
    df2 = pd.DataFrame(data=data_aq2)
    df3 = pd.DataFrame(data=data_aq3)
    df4 = pd.DataFrame(data=data_aq4)
    return (df1, df2, df3, df4)


if __name__ == '__main__':
    main()

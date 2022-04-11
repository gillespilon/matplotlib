#! /usr/bin/env python3
"""
Explore plotting with matplotlib dates

time -f '%e' ./matplotlib_dates.py
./matplotlib_dates.py

References
https://docs.python.org/3/library/datetime.html#module-datetime
https://matplotlib.org/api/dates_api.html#matplotlib-date-format
"""

from typing import Tuple

from numpy.polynomial import polynomial as nppoly
import matplotlib.pyplot as plt
import datasense as ds
import pandas as pd


def main():
    output_url = "matplotlib_figure_axes.html"
    header_title = "matplotlib_figure_axes"
    header_id = "matplotlib-figure-axes"
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
    figsize = (8, 6)
    metadata_dict = {
        "Creator": "Gilles Pilon",
        "Publisher": "Gilles Pilon",
        "Title": "Single figure, single axes graph",
        "Keywords": ["matplotlib", "figure", "axes"],
        "Rights": "Copyright 2020 Gilles Pilon",
    }
    colour1 = "#0077bb"
    colour2 = "#33bbee"
    colour3 = "#cc3311"
    colour4 = "#009988"
    df = ds.read_file(file_name="weight.csv", parse_dates=["Date"])
    # Single figure, single axes
    fig_title = "Figure title"
    axes_title = "Axes title"
    x_axis_label = "X axis label (units)"
    y_axis_label = "Y axis label (units)"
    fig, ax = ds.plot_line_x_y(X=df["Date"], y=df["Steps"], figsize=figsize)
    ax.axhline(y=df["Steps"].median(), xmin=0.05, xmax=0.95, color=colour2)
    middle_titles = (fig.subplotpars.left + fig.subplotpars.right) / 2
    fig.suptitle(
        t=fig_title, x=middle_titles, horizontalalignment="center",
        verticalalignment="top", fontsize=15, fontweight="bold",
    )
    ax.set_ylabel(
        ylabel=y_axis_label, loc="center", fontsize=12, fontweight="semibold"
    )
    ax.set_xlabel(
        xlabel=x_axis_label, loc="center", fontsize=12, fontweight="semibold"
    )
    ax.set_title(
        label=axes_title, loc="center", horizontalalignment="center",
        verticalalignment="top", fontsize=12, fontweight="semibold",
    )
    ds.format_dates(fig=fig, ax=ax)
    ds.despine(ax=ax)
    fig.savefig(
        fname="single_figure_single_axes.svg", format="svg",
        metadata=metadata_dict
    )
    ds.html_figure(file_name="single_figure_single_axes.svg")
    # Single figure, single axes, left y axis, right y axis
    fig_title = "Figure title"
    axes_title = "Axes title"
    x_axis_label = "X axis label (units)"
    left_y_axis_label = "Left vertical axis (units)"
    right_y_axis_label = "Right vertical axis (units)"
    fig, ax1, ax2 = ds.plot_scatterleft_scatterright_x_y1_y2(
        X=df["Date"], y1=df["Actual"], y2=df["Steps"], figsize=figsize,
        linestyle2="-"
    )
    middle_titles = (fig.subplotpars.left + fig.subplotpars.right) / 2
    fig.suptitle(
        t=fig_title, x=middle_titles, horizontalalignment="center",
        verticalalignment="top", fontsize=15, fontweight="bold",
    )
    ax1.set_title(label=axes_title, fontweight="bold")
    ax1.set_ylabel(ylabel=left_y_axis_label, fontweight="bold")
    ax1.set_xlabel(xlabel=x_axis_label, fontweight="bold")
    ax2.set_ylabel(ylabel=right_y_axis_label, fontweight="bold")
    ds.format_dates(fig=fig, ax=ax1)
    fig.savefig(
        fname="single_figure_single_axes_left_y_right_y.svg",
        bbox_inches="tight", format="svg", metadata=metadata_dict,
    )
    ds.html_figure(file_name="single_figure_single_axes_left_y_right_y.svg")
    # Single figure, two axes
    axes_title = ["Axes Title I", "Axes Title II"]
    fig = plt.figure(figsize=figsize)
    fig.suptitle(t=fig_title, fontweight="bold")
    for index in range(1, 3):
        ax = fig.add_subplot(1, 2, index)
        ax.plot(
            df["Date"], df["Steps"], marker="o", linestyle="-", color=colour4
        )
        ax.set_title(label=axes_title[index - 1])
        ax.set_ylabel(ylabel=y_axis_label)
        ax.set_xlabel(xlabel=x_axis_label)
        ds.format_dates(fig=fig, ax=ax)
        ds.despine(ax=ax)
    plt.tight_layout(pad=3)
    fig.savefig(
        fname="single_figure_two_axes.svg", format="svg",
        metadata=metadata_dict
    )
    ds.html_figure(file_name="single_figure_two_axes.svg")
    # Single figure, four axes
    axes_title = ["Data set 1", "Data set 2", "Data set 3", "Data set 4"]
    df1, df2, df3, df4 = create_dataframe()
    fig = plt.figure(figsize=figsize)
    fig_title = "Anscombe's Quartet"
    fig.suptitle(t=fig_title, fontweight="bold")
    for index in range(1, 5):
        df = eval(f"df{index}")
        ax = fig.add_subplot(2, 2, index)
        ax.plot(df["x"], df["y"], marker=".", linestyle="", color=colour1)
        b, m = nppoly.polyfit(df["x"], df["y"], 1)
        equation = f"$y = {b:.1f} + {m:.1f}x$"
        ax.plot(df["x"], m * df["x"] + b, "-", color=colour2, label=equation)
        ax.set_ylim(bottom=2, top=14)
        ax.set_xlim(left=2, right=20)
        ax.set_title(label=axes_title[index - 1])
        ax.set_ylabel(ylabel=y_axis_label)
        ax.set_xlabel(xlabel=x_axis_label)
        ax.legend(frameon=False, fontsize=8)
        ds.despine(ax=ax)
    plt.tight_layout(pad=3)
    fig.savefig(
        fname="single_figure_four_axes.svg", format="svg",
        metadata=metadata_dict
    )
    ds.html_figure(file_name="single_figure_four_axes.svg")
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


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


if __name__ == "__main__":
    main()

#! /usr/bin/env python3
"""
Create two simple, side-by-side scatter plots.
"""

import matplotlib.pyplot as plt
import pandas as pd


def main():
    data = {
        "x": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        "y": [
            32, 37, 35, 28, 41, 44, 35, 31, 34, 38, 42, 36, 31, 30, 31, 34,
            36, 29, 32, 31
        ]
    }
    # https://matplotlib.org/stable/gallery/color/color_demo.html
    # https://matplotlib.org/stable/tutorials/colors/colors.html
    colour_one, colour_two = "#0077bb", "#ee7733"
    # create DataFrames
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
    # pydoc pandas.DataFrame
    df = pd.DataFrame(data=data)
    sample_one = df[df["x"] == 1]
    sample_two = df[df["x"] == 2]
    # create Figure, Axes objects
    # https://matplotlib.org/stable/api/figure_api.html
    # class matplotlib.figure.Figure
    # https://matplotlib.org/stable/api/axes_api.html
    # class matplotlib.axes.Axes
    # https://matplotlib.org/stable/api/
    #     figure_api.html#matplotlib.figure.Figure.subplots
    # pydoc matplotlib.figure.Figure.subplots
    fig, (ax1, ax2) = plt.subplots(
        nrows=1,
        ncols=2,
        sharex=True,
        sharey=True
    )
    # create scatter plots
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    # pydoc matplotlib.axes.Axes.plot
    ax1.plot(
        sample_one["y"],
        marker=".",
        markersize=8,
        linestyle="None",
        color=colour_one
    )
    ax2.plot(
        sample_two["y"],
        marker=".",
        markersize=8,
        linestyle="None",
        color=colour_two
    )
    # adjust the padding between and around subplots
    # https://matplotlib.org/stable/api/
    #     figure_api.html#matplotlib.figure.Figure.tight_layout
    # pydoc matplotlib.figure.Figure.tight_layout
    fig.tight_layout()
    # save image as file
    # https://matplotlib.org/stable/api/figure_api.html
    # pydoc matplotlib.figure.Figure.savefig
    fig.savefig(
        fname="fig_ax_scatter_ex_02.svg",
        format="svg"
    )


if __name__ == "__main__":
    main()

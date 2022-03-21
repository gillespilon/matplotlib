#! /usr/bin/env python3
"""
Create a simple scatter plot.
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
    # create DataFrames
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
    # pydoc pandas.DataFrame
    df = pd.DataFrame(data=data)
    sample_one = df[df["x"] == 1]
    # create Figure, Axes objects
    # https://matplotlib.org/stable/api/figure_api.html
    # class matplotlib.figure.Figure
    # https://matplotlib.org/stable/api/axes_api.html
    # class matplotlib.axes.Axes
    # https://matplotlib.org/stable/api/
    #     figure_api.html#matplotlib.figure.Figure.subplots
    # pydoc matplotlib.figure.Figure.subplots
    fig, ax = plt.subplots(nrows=1, ncols=1)
    # create scatter plot
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    # pydoc matplotlib.axes.Axes.plot
    ax.plot(sample_one["y"], linestyle="None", marker=".", markersize=8)
    # save image as file
    # https://matplotlib.org/stable/api/
    #     figure_api.html#matplotlib.figure.Figure.savefig
    # pydoc matplotlib.figure.Figure.savefig
    fig.savefig(fname="fig_ax_scatter_ex_01.svg", format="svg")


if __name__ == "__main__":
    main()

#! /usr/bin/env python3
"""
Create side-by-side scatter plots.
"""

import matplotlib.pyplot as plt
import pandas as pd


def main():
    data = {
        'x': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        'y': [
            32, 37, 35, 28, 41, 44, 35, 31, 34, 38, 42, 36, 31, 30, 31, 34,
            36, 29, 32, 31
        ]
    }
    # create DataFrames
    df = pd.DataFrame(data=data)
    sample_one = df[df['x'] == 1]
    sample_two = df[df['x'] == 2]
    # create Figure, Axes objects
    fig, (ax1, ax2) = plt.subplots(
        nrows=1, ncols=2, sharex=True, sharey=True
    )
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    ax1.plot(sample_one['y'], marker='.', markersize=8, linestyle='None')
    ax2.plot(sample_two['y'], marker='.', markersize=8, linestyle='None')
    # adjust the padding between and around subplots
    fig.tight_layout()
    # save image as file
    fig.savefig(fname="fig_ax_scatter_ex_02.svg", format="svg")


if __name__ == '__main__':
    main()



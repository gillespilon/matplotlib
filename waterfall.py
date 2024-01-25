#! /usr/bin/env python3
"""
It is a visualization of the cumulative effect of sequentially introduced
positive or negative values. These values can be time-based or category-based.

Based on code by Chris Moffitt:
https://pbpython.com/waterfall-chart.html

TODO: add code to read an Excel or csv file.
"""

import matplotlib.pyplot as plt
import datasense as ds
import pandas as pd
import numpy as np


def main():
    # index = [
    #     "Sales",
    #     "Returns",
    #     "Credit fees",
    #     "Rebates",
    #     "Late charges",
    #     "Shipping",
    # ]
    # data = {AMOUNT: [350000, -30000, -7500, -25000, 95000, -7000]}
    # df = pd.DataFrame(data=data, index=index)
    PATH_GRAPH_SVG = "waterfall.svg"
    TITLE = "2014 Sales Waterfall"
    FILE_NAME = "waterfall.xlsx"
    LAST_BAR_COLOUR = "green"
    POSITIVE_COLOUR = "green"
    NEGATIVE_COLOUR = "red"
    LAST_COLUMN = "Net"
    GRID_ALPHA = 0.2
    FORMAT = "svg"
    df = ds.read_file(file_name=FILE_NAME)
    df = df.set_index(df.columns[0])
    amount = df.columns[0]
    df_blank = df[amount].cumsum().shift(1).fillna(0)
    df_total = df.sum()[amount]
    df.loc[LAST_COLUMN] = df_total
    df_blank.loc[LAST_COLUMN] = df_total
    # step is a Series
    step = df_blank.reset_index(drop=True).repeat(3).shift(-1)
    step[1::3] = np.nan
    df_blank.loc[LAST_COLUMN] = 0
    fig, ax = plt.subplots()
    x = df.index  # bar positions
    # create the waterfall chart, no need for a stacked argument
    ax.bar(x=x, height=df[amount], width=0.4, bottom=df_blank)
    # set bar colors based on values
    for i, p in enumerate(ax.patches):
        if df.iloc[i][amount] > 0:
            p.set_facecolor(POSITIVE_COLOUR)
        else:
            p.set_facecolor(NEGATIVE_COLOUR)
    # Change color of the last bar (index -1) to green
    # ax.patches contains a list of bar objects in the plot
    # ax.patches[-1] accesses the last bar in that list
    # last_bar = ax.patches[-1]
    # last_bar.set_facecolor(LAST_BAR_COLOUR)  # set desired color here
    ax.plot(step.index, step.values, "b", linewidth=0.5)
    ax.tick_params(axis="x", labelsize=14, labelrotation=90)
    ax.tick_params(axis="y", labelsize=14)
    ax.grid(visible=True, which="major", axis="y", alpha=GRID_ALPHA)
    ax.set_ylabel(ylabel="ylabel", weight="bold", fontsize=16)
    ax.set_xlabel(xlabel="xlabel", weight="bold", fontsize=16)
    ax.set_title(label=TITLE, weight="bold", fontsize=18)
    ds.despine(ax=ax)
    fig.savefig(fname=PATH_GRAPH_SVG, format=FORMAT, bbox_inches="tight")
    print(df)


if __name__ == "__main__":
    main()

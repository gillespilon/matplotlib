#! /usr/bin/env python3
"""
Normal probability plot.

Mathematical outputs:
    theoretical quantiles (x axis)
    ordered responses (y axis)
    slope of the least-squares fit line
    intercept of the least-squares fit line
    r is the square root of the coefficient of determination
"""

from pathlib import Path

from matplotlib.offsetbox import AnchoredText
import matplotlib.pyplot as plt
from scipy import stats
import datasense as ds


def main():
    colour1, colour2 = "#0077bb", "#33bbee"
    axes_label = "Normal Probability Plot"
    spines_to_remove = ["top", "right"]
    ds.style_graph()
    # replace next line(s) with your data Series
    # df = ds.read_file(file_name=Path("us_mpg.csv"))
    # s = df.iloc[:, 0]
    # comment out next line if reading your own file
    s = ds.random_data(name="random normal data")
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.spines[spines_to_remove].set_visible(b=False)
    (osm, osr), (slope, intercept, r) = \
        stats.probplot(x=s, dist="norm", fit=True, plot=ax)
    r_squared = r * r
    equation = f"$r^2 = {r_squared:.3f}$"
    ax.get_lines()[0].set(color=colour1, markersize=4)
    ax.get_lines()[1].set(color=colour2)
    ax.set_title(label=f"{axes_label}")
    ax.set_xlabel(xlabel="Theoretical Quantiles")
    ax.set_ylabel(ylabel="Ordered Values")
    text = AnchoredText(s=equation, loc='upper left', frameon=False)
    ax.add_artist(a=text)
    fig.savefig(fname="fig_ax_npp_ex_08.svg", format="svg")


if __name__ == "__main__":
    main()

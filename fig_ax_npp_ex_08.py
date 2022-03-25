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

from matplotlib.offsetbox import AnchoredText
import matplotlib.pyplot as plt

from scipy import stats
import datasense as ds


def main():
    colour1, colour2 = "#0077bb", "#33bbee"
    axes_label = "Normal Probability Plot"
    spines_to_remove = ["top", "right"]
    s = ds.random_data(name="random normal data")
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.spines[spines_to_remove].set_visible(b=False)
    (osm, osr), (slope, intercept, r) = \
        stats.probplot(x=s, dist="norm", fit=True, plot=ax)
    r_squared = r * r
    equation = f"$r^2 = {r_squared:.3f}$"
    ax.get_lines()[0].set(color=colour1, markersize=4)
    ax.get_lines()[1].set(color=colour2)
    ax.set_title(label=f"{axes_label}", fontweight="bold", fontsize=10)
    ax.set_xlabel(xlabel="Theoretical Quantiles", fontweight="bold")
    ax.set_ylabel(ylabel="Ordered Values", fontweight="bold")
    text = AnchoredText(s=equation, loc='upper left', frameon=False)
    ax.add_artist(a=text)
    fig.savefig(fname="fig_ax_scatter_ex_08.svg", format="svg")


if __name__ == "__main__":
    main()

#! /usr/bin/env python3
"""
Histogram with bin size adjustment and tick formatting.
"""

from pathlib import Path

from matplotlib.ticker import StrMethodFormatter
import matplotlib.pyplot as plt
import datasense as ds


def main():
    path_histogram = Path("fig_ax_histogram_ex_11.svg", format="svg")
    s = ds.random_data(size=300)
    ylabel = "Y axis label"
    xlabel = "X axis label"
    title = "Histogram"
    ds.style_graph()
    fig, ax = ds.plot_histogram(
        series=s, bin_range=(-4, 4), number_bins=8, bin_label_bool=True
    )
    ax.set_xlabel(xlabel=xlabel, labelpad=30)
    ax.xaxis.set_major_formatter(formatter=StrMethodFormatter(fmt="{x:0.1f}"))
    ax.set_ylabel(ylabel=ylabel)
    ax.set_title(label=title)
    plt.tight_layout()
    fig.savefig(fname=path_histogram)


if __name__ == "__main__":
    main()

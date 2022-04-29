#! /usr/bin/env python3
"""
Fix issue with ds.plot_histogram for bin_label_bool=True.

Use to enhance example in ds.plot_histogram().
"""

from matplotlib.ticker import StrMethodFormatter
import matplotlib.pyplot as plt
import datasense as ds


def main():
    s = ds.random_data(size=300)
    ds.style_graph()
    # fig, ax = ds.plot_histogram(series=s)
    fig, ax = ds.plot_histogram(
        series=s, bin_range=(-4, 4), number_bins=8, bin_label_bool=True
    )
    ax.set_xlabel(xlabel="x axis label", labelpad=30)
    ax.xaxis.set_major_formatter(
        formatter=StrMethodFormatter(fmt="{x:0.1f}")
    )
    ax.set_ylabel(ylabel="y axis label")
    plt.tight_layout()
    fig.savefig(fname="fix_ds_histogram.svg")


if __name__ == "__main__":
    main()

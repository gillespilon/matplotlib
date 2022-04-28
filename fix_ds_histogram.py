#! /usr/bin/env python3
"""
Fix issue with ds.plot_histogram for bin_label_bool=True.

Use to enhance example in ds.plot_histogram().
"""

import matplotlib.pyplot as plt
import datasense as ds


def main():
    s = ds.random_data(size=100)
    fig, ax = ds.plot_histogram(series=s, bin_label_bool=True)
    ax.set_xlabel(xlabel="x axis label", labelpad=30)
    plt.tight_layout()
    fig.savefig(fname="fix_ds_histogram.svg")


if __name__ == "__main__":
    main()

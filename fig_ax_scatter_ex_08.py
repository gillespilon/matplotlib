#! /usr/bin/env python3
"""
Normal probability plot.
"""

import matplotlib.pyplot as plt

from scipy import stats
import datasense as ds
import pandas as pd


def main():
    df = ds.create_dataframe_norm()
    print(type(df).__name__)


if __name__ == '__main__':
    main()

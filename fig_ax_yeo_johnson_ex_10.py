#! /usr/bin/env python3
"""
Yeo-Johnson normality plot
"""

from pathlib import Path
import time

import matplotlib.pyplot as plt
from scipy import stats
import datasense as ds


def main():
    start_time = time.perf_counter()
    path_yeo_johnson_original = Path("yeo_johnson_original.svg", format="svg")
    path_yeo_johnson = Path("fig_ax_yeo_johnson_ex_10.svg", format="svg")
    path_yeo_johnson_transformed = Path(
        "yeo_johnson_transformed.svg", format="svg"
    )
    colour1 = "#0077bb"
    axes_label = "Normal Probability Plot"
    output_url = "yeo_johnson_plot.html"
    ylabel1 = "Correlation Coefficient"
    xlabel = "Theoretical Quantiles"
    header_title = "Yeo-Johnson Plot"
    header_id = "yeo-johnson-plot"
    ylabel2 = "Ordered Values"
    la, lb = -20, 20
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
    ds.script_summary(script_path=Path(__file__), action="started at")
    ds.style_graph()
    # replace next line(s) with your data Series
    # df = ds.read_file(file_name=Path("us_mpg.csv"))
    # s = df.iloc[:, 0]
    # comment out next line if reading your own file
    s = stats.loggamma.rvs(5, size=500) + 5
    fig, ax = plt.subplots(nrows=1, ncols=1)
    stats.yeojohnson_normplot(x=s, la=la, lb=lb, plot=ax)
    ax.get_lines()[0].set(color=colour1, marker=".", markersize=4)
    yeojohson, maxlog = stats.boxcox(x=s)
    ax.axvline(maxlog, color=colour1, label=f"λ      = {maxlog:7.3f}")
    ax.set_ylabel(ylabel=ylabel1)
    ax.legend(frameon=False, prop={"family": "monospace", "size": 8})
    ds.despine(ax=ax)
    fig.savefig(fname=path_yeo_johnson)
    ds.html_figure(file_name=path_yeo_johnson)
    # create the plot of the untransformed data
    fig, ax = ds.probability_plot(data=s)
    ax.set_title(label=f"{axes_label}")
    ax.set_xlabel(xlabel=xlabel)
    ax.set_ylabel(ylabel=ylabel2)
    fig.savefig(fname=path_yeo_johnson_original)
    ds.html_figure(file_name=path_yeo_johnson_original)
    # create the plot of the transformed data
    fig, ax = ds.probability_plot(data=yeojohson)
    ax.set_title(label=f"{axes_label}")
    ax.set_xlabel(xlabel=xlabel)
    ax.set_ylabel(ylabel=ylabel2)
    fig.savefig(fname=path_yeo_johnson_transformed)
    ds.html_figure(file_name=path_yeo_johnson_transformed)
    stop_time = time.perf_counter()
    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.report_summary(start_time=start_time, stop_time=stop_time)
    ds.html_end(original_stdout=original_stdout, output_url=output_url)
    # plt.show()


if __name__ == "__main__":
    main()

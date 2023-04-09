#! /usr/bin/env python3
"""
Box-Cox normality plot

Requirements
- Series must be > 0

Reference
- https://www.itl.nist.gov/div898/handbook/eda/section3/eda336.htm
- https://www.itl.nist.gov/div898/handbook/eda/section3/boxcox.htm
"""

from pathlib import Path
import time

from scipy import stats
import datasense as ds


def main():
    start_time = time.perf_counter()
    axes_label = "Normal Probability Plot"
    output_url = "box_cox_plot.html"
    xlabel = "Theoretical Quantiles"
    path_box_cox = Path(
        "fig_ax_box_cox_ex_09.svg",
        format="svg"
    )
    path_box_cox_transformed = Path(
        "box_cox_transformed.svg",
        format="svg"
    )
    path_box_cox_original = Path(
        "box_cox_original.svg",
        format="svg"
    )
    header_title = "Box-Cox Plot"
    header_id = "box-cox-plot"
    ylabel2 = "Ordered Values"
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    ds.script_summary(
        script_path=Path(__file__),
        action="started at"
    )
    ds.style_graph()
    # replace next line(s) with your data Series
    # df = ds.read_file(file_name=Path("us_mpg.csv"))
    # s = df.iloc[:, 0]
    # comment out next line if reading your own file
    s = stats.loggamma.rvs(5, size=500) + 5
    fig, ax = ds.plot_boxcox(s=s)
    ax.set_title(label='Box-Cox plot')
    fig.savefig(fname=path_box_cox)
    ds.html_figure(file_name=path_box_cox)
    # create the plot of the untransformed data
    fig, ax = ds.probability_plot(data=s)
    ax.set_title(label=f"{axes_label}")
    ax.set_xlabel(xlabel=xlabel)
    ax.set_ylabel(ylabel=ylabel2)
    fig.savefig(fname=path_box_cox_original)
    ds.html_figure(file_name=path_box_cox_original)
    # create the plot of the transformed data
    boxcox, lmax_mle, (min_ci, max_ci) = stats.boxcox(
        x=s,
        alpha=0.05
    )
    fig, ax = ds.probability_plot(data=boxcox)
    ax.set_title(label=f"{axes_label}")
    ax.set_xlabel(xlabel=xlabel)
    ax.set_ylabel(ylabel=ylabel2)
    fig.savefig(fname=path_box_cox_transformed)
    ds.html_figure(file_name=path_box_cox_transformed)
    stop_time = time.perf_counter()
    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.report_summary(start_time=start_time, stop_time=stop_time)
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


if __name__ == "__main__":
    main()

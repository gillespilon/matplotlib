#! /usr/bin/env python3
"""
List the matplotlib.rcParams.keys().
"""

from pathlib import Path

from matplotlib import rcParams as rc
import datasense as ds


def main():
    output_url = "rcparams_keys.html"
    header_title = "rcParams.keys()"
    header_id = "rcparams-keys"
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    ds.script_summary(
        script_path=Path(__file__),
        action="started at"
    )
    print(rc.keys())
    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


if __name__ == '__main__':
    main()

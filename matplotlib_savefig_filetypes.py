#! /usr/bin/env python3
"""
List the file types for matplotlib.figure.Figure.savefig.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import datasense as ds


def main():
    output_url = "savefig_filetypes.html"
    header_title = "Matplotlib figure.Figure.savefig filetypes"
    header_id = "savefig-filetypes"
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    ds.script_summary(
        script_path=Path(__file__),
        action="started at"
    )
    fig = plt.figure()
    print(fig.canvas.get_supported_filetypes())
    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


if __name__ == '__main__':
    main()

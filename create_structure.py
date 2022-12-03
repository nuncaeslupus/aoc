"""Creates a directory and file structure to code the 50 problems of Advent of Code.

    The structure consists of the year as a base directory, then 25 directories inside
    it numbered from 01 to 25. Inside each ot these daily directories there are three
    files, one for each of the two daily problems and one for data, with the names:
    "1.EXT", "2.EXT" and "data.txt". The extension "EXT" of the code files can be
    modified depending on the language used. The code files are filled with the content
    of the file "example.EXT", which is a template code to read the data file in the
    language set by the extension "EXT"    
"""

import argparse
from argparse_range import range_action
import os
from pathlib import Path
from typing import Optional
import textwrap

days = 4
base_example_file = "example"
base_data_file = "data.txt"
lang_ext = {"python": "py"}


def main(year: str, language: str, base_path: str) -> None:
    ext = lang_ext[language]
    example_file = f"{base_example_file}.{ext}"
    print(example_file)

    for day in range(days):
        new_path = os.path.join(base_path, str(year), str(day + 1).zfill(2))
        try:
            os.makedirs(new_path, exist_ok=True)
        except OSError:
            print(f"Failed creating the directory '{new_path}'.")

        data_file = os.path.join(new_path, base_data_file)
        if not os.path.exists(data_file):
            try:
                open(data_file, "w").close()
            except OSError:
                print(f"Failed creating file '{data_file}.")

        # Copy example base file
        with open(example_file) as f:
            contents = f.read()
            for problem in range(2):
                problem_file = os.path.join(new_path, f"{problem + 1}.{ext}")
                if not os.path.exists(problem_file):
                    try:
                        with open(problem_file, "w") as new_f:
                            new_f.write(contents)
                    except OSError:
                        print(f"Failed creating file '{problem_file}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="create_structure",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=(
            "Creates a directory and file structure for one year of Advent of Code."
        ),
        epilog=textwrap.dedent(
            """\
            Structure example for year 2020, python language and path 'aoc':
            
            aoc
             └─ 2020
                 ├─ 01
                 │  ├─ 1.py
                 │  ├─ 2.py
                 │  └─ data.txt 
                 ├─ 02
                 │  ├─ 1.py
                 │  ├─ 2.py
                 │  └─ data.txt
                 ┆
                 ┆
                 └─ 25
                     ├─ 1.py
                     ├─ 2.py
                     └─ data.txt"""
        ),
    )
    parser.add_argument(
        "year",
        type=int,
        action=range_action(2000, 2099),
        help="a year",
    )
    parser.add_argument(
        "language",
        type=str,
        choices=["python"],
        help="a programming language",
    )
    parser.add_argument(
        "-p",
        "--path",
        type=Path,
        help="a valid path to create the structure (by default the current directory)",
        required=False,
        default=".",
    )

    args = parser.parse_args()
    if not args.path:
        args.path = Path.cwd()
    if not os.path.exists(args.path):
        print(f"Directory {args.path} does not exist.")
    else:
        args.path = os.path.abspath(args.path)

        answer = input(
            f"A folder structure for year {args.year} of Advent of code using the "
            f"{args.language} language is going to be created inside '{args.path}'.\n"
            "No existing files will be overwritten. Continue? (yes/no) "
        )

        while True:
            if answer.lower() in ["y", "yes"]:
                main(args.year, args.language, args.path)
                break
            elif answer.lower() in ["n", "no"]:
                break
            else:
                answer = input("Please answer 'yes' or 'no'. ")

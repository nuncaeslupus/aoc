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
import os
import textwrap
from pathlib import Path

from argparse_range import range_action

days = 25
base_example_file = "example"
base_sample_file = "sample.txt"
base_data_file = "data.txt"
lang_ext = {"python": "py"}


def main(year: str, language: str, base_path: str) -> None:
    ext = lang_ext[language]
    example_file = f"{base_example_file}.{ext}"

    for day in range(days):

        # Make directories
        new_path = os.path.join(base_path, str(year), str(day + 1).zfill(2))
        try:
            os.makedirs(new_path, exist_ok=True)
        except OSError:
            print(f"Failed creating the directory '{new_path}'.")

        # Make both data files
        data_files = [base_sample_file, base_data_file]
        for file in data_files:
            data_file = os.path.join(new_path, file)
            if not os.path.exists(data_file):
                try:
                    open(data_file, "w").close()
                except OSError:
                    print(f"Failed creating file '{data_file}.")

        # Copy example base file to both problem files
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


def get_data(year: int, day: int):
    # https://adventofcode.com/2021/day/10

    cookies = {
        "_ga": "GA1.2.527594012.1668425664",
        "session": "53616c7465645f5fd3f524662f9d68fc4ae8ac8f80ae7f7c2a336e787890dbcf7addff8ca82e449dcd98843a64199ed7db8109ffb6db3ed91616b15c019aeb52",
        "_gid": "GA1.2.24970747.1669821126",
        "ru": "53616c7465645f5f1ef3590ee7dd436cd8606ee7b45e2efd29eb67d44c58aa88c96f46ab8edd0c07f4bfc2ff21f0a745",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    }

    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        cookies=cookies,
        headers=headers,
    )

    return response.text


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
                print("Finished creating structure. Happy coding!")
                break
            elif answer.lower() in ["n", "no"]:
                break
            else:
                answer = input("Please answer 'yes' or 'no'. ")

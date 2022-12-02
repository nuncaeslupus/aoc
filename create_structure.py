import os
from pathlib import Path
from typing import Optional

days = 25


def main(year: str, base_path: Optional[str] = None) -> None:
    if base_path:
        if not Path.is_dir(base_path):
            print(f"'{base_path}' is not a valid path.")
            return
    else:
        base_path = Path.cwd()

    for day in range(days):
        new_path = os.path.join(base_path, str(year), str(day + 1).zfill(2))
        os.makedirs(new_path, exist_ok=True)
        data_file = os.path.join(new_path, "data.txt")
        if not os.path.exists(data_file):
            try:
                open(data_file, "w").close()
            except OSError:
                print("Failed creating the file")

        for problem in range(2):
            new_file = os.path.join(new_path, f"{problem + 1}.py")
            if not os.path.exists(new_file):
                try:
                    open(new_file, "w").close()
                except OSError:
                    print("Failed creating the file")


if __name__ == "__main__":
    main(2022)

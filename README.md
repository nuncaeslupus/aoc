# Advent of Code

**Python solutions to [Advent of Code](https://adventofcode.com/) across several years, plus a script that scaffolds a year's folders.**

Each year has 25 day folders; each day has one script per puzzle part. The scripts are plain Python with no shared framework, so any one of them runs on its own.

## Layout

```text
2021/ 2022/ 2023/
  01/ ... 25/
    1.py          part one
    2.py          part two
    sample.txt    the example from the puzzle text (some days add sample2.txt, ...)
    data.txt      the puzzle input
create_structure.py   scaffolds a new year from example.py
example.py            template copied into each new 1.py / 2.py
```

## Run a solution

Each script reads `data.txt` (or `sample.txt`) from the current directory, so run it from the day's folder:

```console
$ cd 2023/01 && python3 1.py
Result: 54968
Total time: 0.00351 seconds.
```

Switch between the sample and the real input by editing the `data_file` line at the top of the script.

## Scaffold a new year

```bash
pip install -r requirements.txt
python3 create_structure.py 2024 python      # asks for confirmation; never overwrites files
python3 create_structure.py 2024 python -p ~/aoc
```

Run it from the repository root: it reads `example.py` from the current directory. It creates `YEAR/01..25/` with `1.py`, `2.py`, `sample.txt` and `data.txt`. Only Python is supported.

## Related projects

- [claude-arsenal](https://github.com/nuncaeslupus/claude-arsenal) — spec-driven Claude Code workflow and gated task queue.
- [drawspec](https://github.com/nuncaeslupus/drawspec) — declarative diagram spec → clean SVG/PNG/text, writable by LLMs; MCP server included.
- [doc-control](https://github.com/nuncaeslupus/doc-control) — lets AI agents edit Word documents as tracked changes.
- [literary-critic](https://github.com/nuncaeslupus/literary-critic) — LLM manuscript analysis the way a professional editor would.
- [integral-job-search](https://github.com/nuncaeslupus/integral-job-search) — candidate-centred job search run in Claude Code.

## License

No license file is included; all rights reserved by the author.

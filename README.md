# Advent of Code 2020

Solutions for the [AoC 2020](https://adventofcode.com/2020) puzzles, written in Python.

## Solutions

| Day | Title                                                         | Solution                                      |
|-----|---------------------------------------------------------------|-----------------------------------------------|
| 1   | 🛠️ [Report Repair](https://adventofcode.com/2020/day/1)       | **[day1.py](solutions/aoc2020/day1.py)** ⭐⭐ |
| 2   | 🔑 [Password Philosophy](https://adventofcode.com/2020/day/2) | **[day2.py](solutions/aoc2020/day2.py)** ⭐⭐ |
| 2   | 📉 [Toboggan Trajectory](https://adventofcode.com/2020/day/3) | **[day3.py](solutions/aoc2020/day3.py)** ⭐⭐ |

## Batch running

You can run all (or a subset) the solutions with the `aoc` runner script 
provided by [advent-of-code-data](https://github.com/wimglenn/advent-of-code-data).


```bash
$ cat ~/.config/aocd/tokens.json  # create this file with some auth tokens
{
    "github": "53616c7465645f5f0775...",
    "google": "53616c7465645f5f7238...",
    "reddit": "53616c7465645f5ff7c8...",
    "twitter": "53616c7465645f5fa524..."
}
$ pip install . --editable        # install the aoc runner
$ aoc --years 2020 --days 1 2     # run it!
```

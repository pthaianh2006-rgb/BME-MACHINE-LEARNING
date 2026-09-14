# Git and Python/NumPy practice

This repository contains work on the [Git introduction](https://github.com/aim-lab/mlh-course-material/tree/master/tutorials/BME-336546-C00-Introduction%20to%20Git) and [Python, NumPy and friends](https://github.com/aim-lab/mlh-course-material/tree/master/tutorials/BME-336546-C01-Python%2C%20numpy%20and%20friends) tutorials. The Git exercises are preserved in separate branches, and the Python code and results are on this `submission` branch.

For the Git exercise, I started with `tmp.txt`, committed it, and checked out the initial commit to see the file disappear. I then created two branches:

| Branch | What it contains |
| --- | --- |
| `master` | `tmp.txt` with `Hello MLH course!` |
| `example` | The same file with `This is an example` on the next line |
| `example2` | An empty `tmp2.txt`, plus the change merged from `example` |

The original tutorial uses GitHub Classroom and Sourcetree. This exercise was done in this repository with Git commands instead. The exercise commits use the local author name `Tutorial Automation`.

For the Python tutorial, I ran all 112 code cells with Python 3.12 and NumPy 2.3. The two prediction questions came out as `[0, 1, 2, 1]` for filtering values below 3 and `[0, 1, 1, 2, 3, 6, 8]` for quicksort. I used an existing Python installation, so the Conda and Jupyter setup steps were not part of this run.

The main files are:

- [`python_tutorial.py`](python_tutorial.py) — the tutorial examples as a standalone Python script.
- [`python_results.txt`](python_results.txt) — output from every code cell.
- [`git_results.txt`](git_results.txt) — the Git commands and their results.
- [`report/index.html`](report/index.html) — a browsable version of the results.

To run the Python script locally, install the dependency in `requirements.txt`, then run `python python_tutorial.py`.

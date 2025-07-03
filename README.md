# 460-Final
# Smart Email Campaign Optimizer

This project implements two algorithms — a Dynamic Programming (DP) solution and a Greedy approach — to optimize email scheduling for maximum expected conversions. It simulates a marketing scenario where each email has a conversion probability, cooldown time, and a final deadline.

## Features

- Dynamic Programming solution for optimal campaign planning
- Greedy algorithm for quick baseline comparison
- Test suite with 5 non-trivial real-world inspired datasets
- Gantt chart visualizations (optional)
- Easily extendable and modular design

## Files

- `DP.py` – Optimal scheduling using Dynamic Programming
- `greedy.py` – Greedy baseline scheduler
- `full_test_suite.py` – Unified runner with 5 test cases
- `gantt_chart.py` – Plotting function to visualize schedules
- `requirements.txt` – Python package dependencies

## Run Instructions

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all test cases and see comparisons:

```bash
python full_test_suite.py
```

## Test Case Summary

Each test case includes:
- A list of emails, where each is defined as `(conversion_probability, cooldown_days, deadline)`
- A total number of days allowed for the campaign
- Output includes conversion scores and email schedules for both DP and Greedy algorithms

# ISM3232 Midterm: Seabreeze Inn

Name: Luke Mikhail
Version: 1.0
Date: October 25, 2026

## What This Program Does
This program helps calculate the costs of hotel stays at Seabreeze Inn. It can apply discounts, check if a credit check is needed, and see if they are eligible for a welcome package. It lays out the stays and their totals too.

## Business Rules
Stays under 4 nights do not get a standard discount.
Stays of 4 to 13 nights receive a 6% discount.
Stays of 14 or more nights receive an 18% discount.
Corporate guests receive at least a 6% discount.
A $40 cleaning fee is added when the discounted room cost is $300 or less.
Stays totaling $2,000 or more require a credit check.
Guests staying more than 5 nights with a total of at least $1,000 receive a welcome package.

## How to Run
```bash

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

## How to Test
```bash
pytest -v
ruff check .
ruff format .
```

## Files in this Repository
business_rules.py– Calculates stay costs and applies the hotel rules.
main.py– Runs the program and prints the report.
commands.md– Shows the terminal commands I used.
requirements.txt– Lists the packages for the project.
.gitignore– Tells Git what to ignore
README.md– Explains the project.
tests/__init__.py– Helps set up the tests folder.
tests/test_business_rules.py– Has my 20 tests.

## AI Use Statement: Didn't use AI on this exam
Terminal Record: Seabreeze Inn

1. Building the project

```bash
cd ~
mkdir ism3232-midterm
cd ism3232-midterm
pwd
git init
git branch -M main
git status
pwd
clear
pwd
touch business_rules.py main.py commands.md README.md requirements.txt .gitignore
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
ls
ls tests
deactivate
python -m venv .venv
python3 -m venv .venv
source .venv/bin/activate
which python
python -m pip install pytest ruff
pytest --version
ruff --version
printf '.venv/\n__pycache__/\n' > .gitignore
cat .gitignore
printf '.venv/\n__pycache__/\n' > .gitignore
cat .gitignore
printf '.venv/\n__pycache__/\n' > .gitignore
cat .gitignore
python -m pip freeze > requirements.txt
cat requirements.txt
git remote add origin "$(printf 'https://%s/%s/%s.git' github.com lukemikhail ism3232-midterm)"
git remote -v
code .
git status
git add business_rules.py
git commit -m "first function"
git add business_rules.py
git commit -m "add business rules"
git add main.py
git commit -m "main.py"
git add tests/test_business_rules.py
git commit -m "add business rules tests"
git push -u origin main
```

2. The virtual environment

**Command:**

```bash
which python3
```

**Output:**

```
/Users/samermikhail/ism3232-midterm/.venv/bin/python3
```

It shows that my virtual environment is active.

3. The project structure
**Command**

```bash
tree -L 2
```

**Output**

```text
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The .venv folder is on my computer but not in the GitHub repository because it is in .gitignore

4. Every function and test

**Command:**

```bash
rg 'def '
```

**Output:**

```
business_rules.py
11:def calculate_room_cost(nightly_rate: float, nights: int) -> float:
16:def get_stay_discount(nights: int, corporate: bool = False) -> float:
25:def calculate_stay_total(nightly_rate: float, nights: int, corporate: bool = False) -> float:
37:def requires_credit_check(total: float) -> bool:
42:def gets_welcome_package(nights: int, total: float) -> bool:
47:def total_reserved(stays: list) -> float:
61:def largest_stay(stays: list) -> str:
80:def format_stay_line(guest: str, total: float, credit_check: bool, welcome_package: bool) -> str:

tests/test_business_rules.py
3:def test_calculate_room_cost():
7:def test_calculate_stay_total():
11:def test_requires_credit_check():
16:def test_credit_check_threshold():
20:def test_credit_check_below_threshold():
23:def test_gets_welcome_package():
28:def test_welcome_package_at_night_limit():
32:def test_welcome_package_at_total_limit():
37:def test_get_stay_discount():
44:def test_get_stay_discount_at_4_nights():
48:def test_long_stay_discount_at_14_nights():
51:def test_no_discount_under_four_nights():
55:def test_total_reserved():
65:def test_largest_stay():
75:def test_largest_stay_with_tie():
84:def test_largest_stay_with_empty_list():
90:def test_total_reserved_with_empty_list():
96:def test_format_stay_line():
100:def test_cleaning_fee_applied():
106:def test_cleaning_fee_not_applied():
```

There are 8 functions in business_rules.py and 20 tests in tests/test_business_rules.py.

5. Which files print

**Command**

```bash
rg -l 'print'
```

**Output**

```
main.py
```

main.py file uses print for display, but the business_rules.py calculates everything

6. The commit history

**Command:**

```bash
git log --oneline
```

**Output:**

```
bbe93c1 (HEAD -> main, origin/main) add business rules tests
d6acc5b main.py
33fd47a add business rules
f5e17b1 first function
```

There were 4 commits before I committed commands.md
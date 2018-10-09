# microfinder

An Unicode character finder REST API for demonstration purposes.

## Installation

```bash
$ python3 --version
Python 3.7.0
$ python3 -m venv .venv
$ . .venv/bin/activate
(.venv) $ pip install --upgrade pip
Collecting pip
[...]
Successfully installed pip-18.1
(.venv) $ pip install -r requirements.txt
Collecting pytest==3.8.2 (from -r requirements.txt (line 1))
[...]
Collecting Quart==0.6.7 (from -r requirements.txt (line 2))
[...]
Successfully installed MarkupSafe-1.0 Quart-0.6.7 [...] pytest-3.8.2 [...]
```

## Running tests

```bash
$ pytest --disable-warnings
======================================== test session starts ========================================
platform darwin -- Python 3.7.0, pytest-3.8.2, py-1.6.0, pluggy-0.7.1
rootdir: /Users/lramalho/prj/tw/microfinder, inifile:
collected 10 items

index/index_test.py .......                                                                   [ 70%]
name/name_test.py ...                                                                         [100%]

=============================== 10 passed, 9 warnings in 2.29 seconds ===============================

```
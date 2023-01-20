#!/bin/sh

# Linter checks
# stop the build if there are Python syntax errors or undefined names
echo "***** Linter: Checking Python syntax errors *****"
flake8 ./app_home/* --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 ./app_english_dic/* --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 ./app_todo/* --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 ./app_users/* --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 ./utils/* --count --select=E9,F63,F7,F82 --show-source --statistics

# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
echo "***** Linter: Checking Python syntax patterns *****"
flake8 ./app_home/* --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
flake8 ./app_english_dic/* --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
flake8 ./app_todo/* --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
flake8 ./app_users/* --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
flake8 ./utils/* --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Unit test and coverage
echo "***** Unit Test *****"
coverage run -m pytest -v -s
echo "***** Coverage tests *****"
coverage report --omit="*/tests/*,*/venv/*" -m ./falken_teleworking/*.py 

# Coverage report in html
# coverage run -m pytest -v && coverage html --omit="*/test/*,*/venv/*"

# With param -s for input
# coverage run -m pytest -v -s && coverage html --omit="*/test/*,*/venv/*"

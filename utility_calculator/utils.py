# -*- coding: utf-8 -*-
"""utilities that would clutter the main file"""
import os
import re
from utility_calculator import db_path
from utility_calculator.db_functions import create_database


# TODO (jam) rename this file
def check_db():
    """create the database if it doesn't exist"""
    if not os.path.exists(db_path):
        create_database()


def choose(prompt, options):
    """return a value that matches a given option from options"""
    while True:
        option = clean_input(prompt)
        if option in options:
            return option
        print("Please choose between: ", *options)


def clean_input(prompt):
    """return user input to a prompt, casefolded and stripped of whitespace"""
    return input(prompt).casefold().strip()


def confirm(prompt=None):
    """return True if user confirmed (entered 'y' or 'yes'), otherwise return False"""
    if not prompt:
        prompt = "Does this information look correct? [Y/n] "
    return clean_input(prompt) in ("y", "yes")


def get_float(prompt):
    """return user input to a prompt as a float"""
    while True:
        try:
            var = float(input(prompt))
            return var
        except ValueError:
            print("Please enter a valid number!")
            continue


def get_month():
    """ask the user for the month and ensure correct formatting"""
    month_regex = re.compile(r"\d{4}-(0[1-9]|1[0-2])")
    while True:
        month = input("Enter the month: ")
        if re.search(month_regex, month):
            return month
        print("Please enter month as 'YYYY-MM'")

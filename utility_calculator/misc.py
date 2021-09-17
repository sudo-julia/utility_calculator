# -*- coding: utf-8 -*-
"""utilities that would clutter the main file"""
import re
import sys
from typing import Pattern, Tuple, Union


def choose(prompt: str, options: Tuple) -> str:
    """Returns a value that matches a given option from options

    Args:
        prompt (str): The prompt to display to the user
        options (Tuple): A tuple of choices that the user can select from

    Returns:
        str: The string selected from 'options'
    """
    while True:
        option: str = clean_input(prompt)
        if option in options:
            return option
        print("Please choose between: ", *options)


def clean_input(prompt: str) -> str:
    """Returns user input to a prompt, casefolded and stripped of whitespace

    Args:
        prompt (str): The prompt to display to the user

    Returns:
        str: The user's input to the prompt
    """
    return input(prompt).casefold().strip()


def confirm(prompt: str = None) -> bool:
    """Confirms a choice made by the user

    Args:
        prompt (str): The prompt to display to the user (default is None)

    Returns:
        bool: True if the user entered 'y' or 'yes', False otherwise
    """
    if not prompt:
        prompt = "Does this information look correct? [Y/n] "
    return clean_input(prompt) in ("y", "yes")


def get_float(prompt: str) -> float:
    """Returns user input to a prompt as a float

    Args:
        prompt (str): The prompt to display to the user

    Returns:
        float: The float input by the user
    """
    while True:
        try:
            var: float = float(input(prompt))
            return var
        except ValueError:
            print("Please enter a valid number!")
            continue


def get_month() -> str:
    """Asks the user for the month and ensures correct formatting

    Returns:
        str: A month of a year, formatted as 'YYYY-MM'
    """
    month_regex: Pattern[str] = re.compile(r"^(?:\d{4}-(?:0[1-9]|1[0-2]))$")
    while True:
        month: str = clean_input("Enter the month: ")
        if re.search(month_regex, month):
            return month
        print("Please enter month as 'YYYY-MM' (ex: 2021-10)")


def print_error(error: Union[str, Exception]) -> None:
    """Prints a message to stderr

    Args:
        error (str): The error message to print
    """
    print(error, file=sys.stderr)

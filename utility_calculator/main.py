# -*- coding: utf-8 -*-
"""utility calculator"""
from __future__ import annotations
import json
from utility_calculator import db_functions
import utility_calculator.utils as utils


def menu():
    """run the menu"""
    print("\nSelect from the following menu options:")
    select = utils.clean_input(
        "1. Utility Calculator (u)\n2. New Roommate (n)\n3. Exit (e)\n> "
    )
    if select in ("u", 1):
        sum_utilites()
    elif select in ("n", 2):
        new_person()
    elif select in ("e", 3):
        raise SystemExit


# TODO (jam) redundancy in this and utility_calc?
def sum_utilites():
    """grab the cost of individual utilities and find the sum"""
    water = utils.validate_float("Enter the water bill: $")
    gas = utils.validate_float("Enter the gas bill: $")
    internet = utils.validate_float("Enter the internet bill: $")
    electricity = utils.validate_float("Enter the electrical bill: $")

    total = water + gas + internet + electricity
    print(f"Utility Total: ${total}")

    utility_calc(total)

    select = utils.clean_input(
        "Would you like to return to the main menu (m) or exit the program (e)?\n> "
    )

    if select == "m":
        menu()
    elif select == "e":
        raise SystemExit


def utility_calc(total):
    """perform the calculation of utilities"""
    # TODO (jam) overhaul, fetch data from database
    with open("test.json", "r") as json_file:
        json_data = json.load(json_file)
    # iterate through json data to add up number of roommates, cats, etc.
    num_roommates = 0
    num_cats = 0
    for roommate in json_data:
        if roommate["type"] == "roommate":
            num_roommates += 1
        elif roommate["type"] == "cat":
            num_cats += 1
        elif roommate["type"] == "kiln":
            # TODO (jam) kiln operations
            kiln_cost = input("Input kiln cost: $")
            total = total - kiln_cost
    total_per = round(total / num_roommates, 2)
    print(f"${total_per}")


def new_bill():
    """add a bill to the database"""
    utils.check_db()

    while True:
        # month = utils.get_month()
        raise NotImplementedError


def new_person():
    """add a new person to the list of roommates"""
    utils.check_db()

    # TODO (jam) standardize this (>) and create function to check month formatting
    #            as YYYY-MM
    while True:
        month = utils.get_month()
        time_spent = utils.validate_float("Enter the amount of time spent home: ")
        name = utils.clean_input("Enter the person's name: ").title()

        print(f"Month: {month}, Time spent at house: {time_spent}, Name: {name}")
        if utils.confirm("Does this information look correct? [Y/n] "):
            break

    db_functions.add_roommate(month, time_spent, name)


# Total cost of utilties -> calculate kiln cost, subtract kiln cost
# -> calculate price per day for bill period ->
# Charge cats and subtract that from total ->
# divide total remaining cost by number of roommates -> charge roommates

if __name__ == "__main__":
    menu()

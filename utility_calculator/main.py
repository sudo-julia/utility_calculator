# -*- coding: utf-8 -*-
"""utility calculator"""
from __future__ import annotations
import json
from datetime import datetime
from utils import clean_input, validate_float


def menu():
    """run the menu"""
    print("\nSelect from the following menu options:")
    select = clean_input(
        "1. Utility Calculator (u)\n2. New Person (n)\n3. Exit (e)\n> "
    )
    if select in ("u", 1):
        utility_sum()
    elif select in ("n", 2):
        new_person()
    elif select in ("e", 3):
        raise SystemExit


def utility_sum():
    """grab the cost of individual utilities and find the sum"""
    water = validate_float("Enter the water bill: $")
    gas = validate_float("Enter the gas bill: $")
    internet = validate_float("Enter the internet bill: $")
    electricity = validate_float("Enter the electrical bill: $")

    total = water + gas + internet + electricity
    print(f"Utility Total: ${total}")

    utility_calc(total)

    select = clean_input(
        "Would you like to return to the main menu (m) or exit the program (e)?\n> "
    )

    if select == "m":
        menu()
    elif select == "e":
        raise SystemExit


def utility_calc(total):
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
            return total
    total_per = round(total / num_roommates, 2)
    print(f"${total_per}")


def new_person():
    """add a new person to the list of roommates"""
    user_input = clean_input(
        "Would you like to add a new person or item? Choose (y) or (n): "
    )
    if user_input == "y":
        with open("test.json", "r") as json_file:
            json_data = json.load(json_file)

        new_name = input("Name: ")
        new_type = input("Type (human, cat, item): ")
        new_dict = {"name": new_name, "type": new_type}

        date = datetime.now()
        timestamp = str(round(datetime.timestamp(date)))

        json_data["dt"] = timestamp
        json_data["people"].append(new_dict)

        with open("test.json", "w") as json_file:
            json.dump(json_data, json_file, indent=4)

    elif user_input == "n":
        menu()
    elif user_input == "e":
        raise SystemExit
    else:
        menu()


# Use a chain map for default settings when intializing new list info.

# Total cost of utilties -> calculate kiln cost, subtract kiln cost
# -> calculate price per day for bill period ->
# Charge cats and subtract that from total ->
# divide total remaining cost by number of roommates -> charge roommates

# Complete: Create function that adds new roommate/cat to main database
# if water month then factor in 2 month cost with days of cats

if __name__ == "__main__":
    menu()

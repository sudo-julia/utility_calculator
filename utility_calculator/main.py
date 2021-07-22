# -*- coding: utf-8 -*-
"""utility calculator"""
from utility_calculator import db_path
import utility_calculator.misc as misc
from utility_calculator.database import Database

# TODO (jam) option for user to specify location
database = Database(db_path)


def menu():
    """run the menu"""
    print("\nSelect from the following menu options:")
    selection = misc.choose(
        "1. Utility Calculator (u)\n2. New Roommate (n)\n3. Exit (e)\n> ",
        ("u", "n", "e"),
    )
    if selection == "u":
        utility_calc()
    elif selection == "n":
        new_person()
    elif selection == "e":
        raise SystemExit


def utility_calc(quick=None):
    """grab the cost of individual utilities and find the sum"""
    # TODO (jam) change this to read from database OR insert all values
    water = misc.get_float("Enter the water bill: $")
    gas = misc.get_float("Enter the gas bill: $")
    internet = misc.get_float("Enter the internet bill: $")
    electricity = misc.get_float("Enter the electrical bill: $")

    total = water + gas + internet + electricity
    print(f"Utility Total: ${total}")

    if quick:
        num_roommates = int(misc.clean_input("Enter the number of roommates: "))
        print(f"Each roommate pays {total / num_roommates:.2f}")
        raise SystemExit

    sum_utilities(total)

    selection = misc.choose(
        "Would you like to return to the main menu (m) or exit the program (e)?\n> ",
        ("m", "e"),
    )

    if selection == "m":
        menu()
    elif selection == "e":
        raise SystemExit


def sum_utilities(total):
    """perform the calculation of utilities"""
    # TODO (jam) overhaul, fetch data from database
    print(total)
    raise NotImplementedError


def new_bill():
    """add a bill to the database"""
    # TODO (jam) let the user manually input the type of bill
    #            once the database has entries, it can suggest from existing bill types
    database.create_database()
    bills = ("water", "power", "gas", "internet")

    while True:
        month = misc.get_month()
        category = misc.choose("Water, power, gas or internet bill? ", bills)
        cost = misc.get_float(f"Enter the cost of the {category} bill: ")
        paid = int(misc.confirm("Was the bill paid? [Y/n] "))
        paid_str = "unpaid"
        if paid:
            paid_str = "paid"

        print(f"The {category} bill for {month} cost {cost} and was {paid_str}.")
        if misc.confirm():
            break

    database.add_bill(month, category, cost, paid)


def new_person():
    """add a new person to the list of roommates"""
    misc.check_db(database)

    while True:
        month = misc.get_month()
        # TODO (jam) validate this
        time_spent = float(
            misc.clean_input("Enter the percentage of time spent home: ").strip("%")
        )
        name = misc.clean_input("Enter the person's name: ").title()

        print(f"Month: {month}, Time spent at house: {time_spent}, Name: {name}")
        if misc.confirm():
            break

    database.add_roommate(month, time_spent, name)


# Total cost of utilties -> calculate kiln cost, subtract kiln cost
# -> calculate price per day for bill period ->
# Charge cats and subtract that from total ->
# divide total remaining cost by number of roommates -> charge roommates

if __name__ == "__main__":
    menu()

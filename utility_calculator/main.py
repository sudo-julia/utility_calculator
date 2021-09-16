# -*- coding: utf-8 -*-
"""utility calculator"""
from utility_calculator import database
import utility_calculator.misc as misc


def menu():
    """Run the main menu"""
    print("\nSelect from the following menu options:")
    selection: str = misc.choose(
        "1. Utility Calculator (u)\n2. New Roommate (n)\n3. Exit (e)\n> ",
        ("u", "n", "e"),
    )
    if selection == "u":
        utility_calc()
    elif selection == "n":
        new_person()
    elif selection == "e":
        raise SystemExit


def utility_calc(quick: bool = False):
    """Calculates the cost of utilties

    Args:
        quick (bool): Whether or not to run the 'quick' version of the script
                      (defaults to False)
    """
    # TODO: (jam) change this to read from database OR insert all values
    water: float = misc.get_float("Enter the water bill: $")
    gas: float = misc.get_float("Enter the gas bill: $")
    internet: float = misc.get_float("Enter the internet bill: $")
    electricity: float = misc.get_float("Enter the electrical bill: $")

    total: float = water + gas + internet + electricity
    print(f"Utility Total: ${total}")

    if quick:
        num_roommates: int = int(misc.clean_input("Enter the number of roommates: "))
        print(f"Each roommate pays {total / num_roommates:.2f}")
        raise SystemExit

    sum_utilities(total)

    selection: str = misc.choose(
        "Would you like to return to the main menu (m) or exit the program (e)?\n> ",
        ("m", "e"),
    )

    if selection == "m":
        menu()
    elif selection == "e":
        raise SystemExit


def sum_utilities(total: float):
    """Performs the calculation of utilities

    Args:
        total (float): The total of all utilities
    """
    # TODO: (jam) overhaul, fetch data from database
    print(total)
    raise NotImplementedError


def new_bill():
    """UI for adding a bill to the database"""
    # TODO: (jam) let the user manually input the type of bill
    #            once the database has entries, it can suggest from existing bill types
    bills: tuple = ("water", "power", "gas", "internet")

    while True:
        month: str = misc.get_month()
        category: str = misc.choose("Water, power, gas or internet bill? ", bills)
        cost: float = misc.get_float(f"Enter the cost of the {category} bill: ")
        # this bool must be converted to an int, as sqlite3 doesn't have a bool type
        paid: int = int(misc.confirm("Was the bill paid? [Y/n] "))
        if paid:
            paid_str = "paid"
        else:
            paid_str = "unpaid"

        print(f"The {category} bill for {month} cost {cost} and was {paid_str}.")
        if misc.confirm():
            break
        print("Restarting selection process.")

    if not database.add_bill(month, category, cost, paid):
        print(f"Failed to add {category} bill to the database.")


def new_person():
    """UI for adding a roommate to the database"""
    while True:
        month: str = misc.get_month()
        time_spent: float = float(
            misc.clean_input("Enter the percentage of time spent home: ").strip("%")
        )
        name: str = misc.clean_input("Enter the person's name: ").title()

        print(f"Month: {month}, Time spent at house: {time_spent}, Name: {name}")
        if misc.confirm():
            break

    if not database.add_roommate(month, time_spent, name):
        print(f"Failed to add {name} to the database.")


# Total cost of utilties -> calculate kiln cost, subtract kiln cost
# -> calculate price per day for bill period ->
# Charge cats and subtract that from total ->
# divide total remaining cost by number of roommates -> charge roommates

if __name__ == "__main__":
    menu()

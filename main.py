import sys
import json
from datetime import datetime

def menu():
    print("\nSelect from the following menu options:")
    select = input("1. Utility Calculator (u)\n2. New Person (n)\n3. Exit (e)\n: ").casefold()
    if select == "u" or select == "1":
        utility_sum()
    elif select == "n" or select == "2":
        new_person()
    elif select == "e" or select == "3":
        sys.exit()

def utility_sum():
    while True:
        try:
            water = float(input("Give me the water bill: $"))
            print(water)
            gas = float(input("Give me the gas bill: $"))
            print(gas)
            internet = float(input("Give me the internet bill: $"))
            print(internet)
            electricity = float(input("Give me the electrical bill: $"))
            print(electricity)
            break
        except:
            print("Please only input numbers.\n")

    total = water + gas + internet + electricity
    print("Utility Total: $" + str(total))

    utility_calc(total)

    select = input("Would you like to return to the main menu (m) or exit the program (e)?: ")
    if select == "m":
        menu()
    elif select == "e":
        sys.exit()

"""
def validate_input(prompt, float):
    """"""get input and validate type""""""
    while True:
        var = input(prompt)
        if isinstance(var, float):
            return var

types = {'string': str, 'int': int}
"""

def utility_calc(total):
    with open("test.json", "r") as json_file:
        json_data = json.load(json_file)
    # iterate through json data to add up number of roommates, cats, etc.
    for _ in json_data:
        if _["type"] == "roommate":
            num_roommates = 0
            num_roommates += 1
    for _ in json_data:
        if _["type"] == "cat":
            num_cats = 0
            num_cats += 1
    for _ in json_data:
        if _["type"] == "kiln":
            kiln_cost = input("Input kiln cost: $")
            total = total - kiln_cost
            return total
    total_per = round(total / num_roommates, 2)
    print("${}".format(total_per))

def new_person():
        user_input = input("Would you like to add a new person or item? Choose (y) or (n): ").casefold().strip()
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
                json.dump(json_data, json_file, indent = 4)
        elif user_input == "n":
            menu()
        elif user_input == "e":
            sys.exit()
        else:
            menu()

"""
for _ in list:
    if _["type"] == "cat":
        print(_["name"])

for _ in list:
    if _["type"] == "kiln":
        print(_["users"])
        if "clark" in _["users"]:
            print("Da fuk?")
        if "panda" not in _["users"]:
            print("No. Wrong.")
            """

# Use a chain map for default settings when intializing new list info.

# Total cost of utilties -> calculate kiln cost, subtract kiln cost -> calculate price per day for bill period ->
# Charge cats and subtract that from total -> divide total remaining cost by number of roommates -> charge roommates

#Complete: Create function that adds new roommate/cat to main database
# if water month then factor in 2 month cost with days of cats

if __name__ == '__main__':
    print("\n\n---Welcome to the automated Utility Tally of Information system or 'UTI'---")
    menu()



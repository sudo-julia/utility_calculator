"""utilities that would clutter the main file"""


def clean_input(prompt):
    """return user input to a prompt, casefolded and stripped of whitespace"""
    return input(prompt).casefold().strip()


def validate_float(prompt):
    """return user input to a prompt as a float"""
    while True:
        var = input(prompt)
        if isinstance(var, float):
            return var
        print("Please enter a valid number!")

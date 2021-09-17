# -*- coding: utf-8 -*-
"""database operations for utility_calculator"""
from pathlib import Path
import sqlite3

from utility_calculator.misc import print_error


class Database:
    """
    A class used to communicate with a sqlite3 database

    Attributes:
        location (str): the location of the database
    """

    def __init__(self, location: str) -> None:
        """Initialize attributes for the Database class

        Args:
            location (str): The location of the database
        """
        self.location = location
        if not self.create_database():
            print_error("Error creating database! Cancelling...")
            raise SystemExit(1)
        self.connection: sqlite3.Connection = sqlite3.connect(self.location)

    def create_database(self) -> bool:
        """Creates the database at the location provided by self.location

        Returns:
            bool: True if the database was created, False on a failure
        """
        # create parent directory if it doesn't exist
        try:
            parent_dir = Path(self.location).parent
            if not parent_dir.exists():
                parent_dir.mkdir()
        except PermissionError as err:
            print_error(err)
            return False
        # context manager will automatically call conn.commit() when closed
        try:
            with sqlite3.connect(self.location) as conn:
                cur = conn.cursor()
                cur.execute(
                    """CREATE TABLE IF NOT EXISTS bills
                        (month TEXT,
                        category TEXT,
                        cost REAL,
                        paid INT);"""
                )
                cur.execute(
                    """CREATE TABLE IF NOT EXISTS roommates
                        (month TEXT,
                        time_spent REAL,
                        name TEXT);"""
                )
        except sqlite3.Error as err:
            print_error(err)
            return False
        return True

    def add_bill(self, month: str, category: str, cost: float, paid: int) -> bool:
        """Adds a bill to the bills table of the database

        Args:
            month (str): The month to add the bill to
            category (str): The category that the bill falls under (ex: water, gas, etc)
            cost (float): The cost of the bill
            paid (int): Whether or not the bill has been paid, acts as a bool

        Returns:
            bool: True if the operation was successful, False upon failure
        """
        # TODO: check for existing bills/give option to overwrite
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO bills VALUES (?, ?, ?, ?)",
                (month, category, cost, paid),
            )

        if paid:
            paid_str = "paid"
        else:
            paid_str = "unpaid"
        print(f"Added {paid_str} {category} bill valuing {cost} to {month}.")
        return True

    def add_roommate(self, month: str, time: float, name: str) -> bool:
        """Adds a roommate to the roommates table of the database

        Args:
            month (str): The month to add the roommate to
            time (float): The amount of time that the roommate was there (0.00 - 1.00)
            name (str): The roommate's name

        Returns:
            bool: True if the operation was successful, False upon failure
        """
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO roommates VALUES (?, ?, ?)", (month, time, name))

        print(f"Added {name} for {time:1.0%} of {month}.")
        return True

    def query_bills(self, month: str) -> None:
        """Queries the bills for a given month

        Args:
            month (str): The month to query bills for
        """
        # TODO: notify if month doesn't exist
        with self.connection as conn:
            cur = conn.cursor()
            for row in cur.execute("SELECT * FROM bills WHERE month = '?'", (month)):
                print(row)

    def query_roommates(self, month: str) -> None:
        """Queries the roommates for a given month

        Args:
            month (str): The month to query roommates for
        """
        # TODO: notify if month doesn't exist
        with self.connection as conn:
            cur = conn.cursor()
            for row in cur.execute("SELECT * FROM roomates WHERE month = '?'", (month)):
                print(row)

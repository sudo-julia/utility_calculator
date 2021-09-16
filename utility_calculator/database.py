# -*- coding: utf-8 -*-
"""database operations for utility_calculator"""
import os
from pathlib import Path
import sqlite3


# TODO: (jam) document
class Database:
    """
    A class used to communicate with a sqlite3 database

    Attributes:
        location: str
            the location of the database

    Methods:
        create_database(self) -> bool
            Creates the database at the location provided by self.location
        add_bill(self, month: str, category: str, cost: float. paid: int)
            Adds a bill to the bills table of the database
        add_roommate(self, month: str, time: float, name: str)
            Adds a roommate to the roommates table of the database
        query_bills(self, month: str)
            Queries the bills for a given month
        query_roommates(self, month: str)
            Queries the roommates for a given month
        db_exists(self) -> bool:
            Creates the database if it doesn't exist

    """

    def __init__(self, location: str):
        """Initialize attributes for the Database class

        Args:
            location (str): The location of the database
        """
        self.location = location
        # TODO: should this be one method?
        if not self.db_exists():
            self.create_database()
        self.connection: sqlite3.Connection = sqlite3.connect(self.location)

    def create_database(self) -> bool:
        """Creates the database at the location provided by self.location

        Returns:
            bool: True if the database was created, False on a failure
        """
        # TODO: error handling
        # create parent directory if it doesn't exist
        if not (parent_dir := Path(self.location).parent).exists():
            parent_dir.mkdir()
        # context manager will automatically call conn.commit() when closed
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
        print(f"Utility database created at '{self.location}'")
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
        if not self.db_exists():
            self.create_database()
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
        if not self.db_exists():
            self.create_database()
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO roommates VALUES (?, ?, ?)", (month, time, name))

        print(f"Added {name} for {time:0%} of {month}.")
        return True

    def query_bills(self, month: str):
        """Queries the bills for a given month

        Args:
            month (str): The month to query bills for
        """
        # TODO: notify if month doesn't exist
        with self.connection as conn:
            cur = conn.cursor()
            for row in cur.execute("SELECT * FROM bills WHERE month = '?'", (month)):
                print(row)

    def query_roommates(self, month: str):
        """Queries the roommates for a given month

        Args:
            month (str): The month to query roommates for
        """
        # TODO: notify if month doesn't exist
        with self.connection as conn:
            cur = conn.cursor()
            for row in cur.execute("SELECT * FROM roomates WHERE month = '?'", (month)):
                print(row)

    def db_exists(self) -> bool:
        """Creates the database if it doesn't exist

        Returns:
            bool: True if the database exists, False if it doesn't
        """
        if not os.path.exists(self.location):
            return False
        return True

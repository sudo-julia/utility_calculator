# -*- coding: utf-8 -*-
"""database operations for utility_calculator"""
from __future__ import annotations
import sqlite3


# TODO (jam) document
class Database:
    """..."""

    def __init__(self, location):
        """..."""
        self.location = location
        self.connection = sqlite3.connect(location)

    def create_database(self):
        """create a database with the default tables"""
        # context manager will automatically call conn.commit() when closed
        # TODO (jam) see if this will call commit
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(
                """CREATE TABLE bills
                    (month TEXT,
                    category TEXT,
                    cost REAL,
                    paid INT);"""
            )
            cursor.execute(
                """CREATE TABLE roommates
                    (month TEXT,
                    time_spent REAL,
                    name TEXT);"""
            )
        print(f"Utility database created at {self.location}.")

    def add_roommate(self, month, time, name):
        """add a roommate to the roommates table"""
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO roommates VALUES (?, ?, ?)", (month, time, name)
            )
        print(f"Added {name} for {time:0%} of {month}.")

    def add_bill(self, month, category, cost, paid):
        """add a bill to the bills table"""
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO bills VALUES (?, ?, ?, ?)",
                (month, category, cost, paid),
            )
        if paid:
            paid = "paid"
        else:
            paid = "unpaid"
        print(f"Added {paid} {category} bill valuing {cost} to {month}.")

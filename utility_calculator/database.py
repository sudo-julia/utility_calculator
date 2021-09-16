# -*- coding: utf-8 -*-
"""database operations for utility_calculator"""
import os
from pathlib import Path
import sqlite3


# TODO: (jam) document
class Database:
    """..."""

    def __init__(self, location):
        """..."""
        self.location = location
        if not Path(location).exists():
            self.create_database()
        self.connection = sqlite3.connect(self.location)

    def create_database(self):
        """create a database with the default tables"""
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
        return True

    def add_bill(self, month, category, cost, paid):
        """add a bill to the bills table"""
        self.check_db()
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO bills VALUES (?, ?, ?, ?)",
                (month, category, cost, paid),
            )
        if paid:
            paid = "paid"
        else:
            paid = "unpaid"
        print(f"Added {paid} {category} bill valuing {cost} to {month}.")

    def add_roommate(self, month, time, name):
        """add a roommate to the roommates table"""
        self.check_db()
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO roommates VALUES (?, ?, ?)", (month, time, name))
        print(f"Added {name} for {time:0%} of {month}.")

    def query_bills(self, month):
        """query the bills for a month"""
        with self.connection as conn:
            cur = conn.cursor()
            for row in cur.execute("SELECT * FROM bills WHERE month = '?'", (month)):
                print(row)

    def query_roommates(self, month):
        """query the roommates for a month"""
        with self.connection as conn:
            cur = conn.cursor()
            for row in cur.execute("SELECT * FROM roomates WHERE month = '?'", (month)):
                print(row)

    def check_db(self):
        """create the database if it doesn't exist"""
        if not os.path.exists(self.location):
            if self.create_database():
                print(f"Utility database created at {self.location}")

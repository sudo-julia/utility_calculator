# -*- coding: utf-8 -*-
"""database operations for utility_calculator"""
from __future__ import annotations
import sqlite3
from utility_calculator import db_path


def create_database():
    """create a database with the default tables"""
    # context manager will automatically call conn.commit() when closed
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE bills
                (month TEXT,
                start TEXT,
                end TEXT,
                category TEXT,
                cost REAL,
                paid INT);"""
        )
        cursor.execute(
            """CREATE TABLE roommates
                (month TEXT,
                time REAL,
                name TEXT);"""
        )
    print(f"Utility database created at {db_path}.")


def add_roommate(month, time, name):
    """add a roommate to the roommates table"""
    with sqlite3.connect("utility_calculator.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO roommates VALUES (?, ?, ?)", (month, time, name))


# pylint: disable=too-many-arguments
def add_bill(month, start, end, category, cost, paid):
    """add a bill to the bills table"""
    with sqlite3.connect("utility_calculator.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO bills VALUES (?, ?, ?, ?, ?, ?)",
            (month, start, end, category, cost, paid),
        )

# -*- coding: utf-8 -*-
from utility_calculator.database import Database
from utility_calculator.user_data_dir import user_data_dir


DB_PATH: str = f"{user_data_dir('utility_calculator')}/utility_calculator.db"
database = Database(DB_PATH)

# -*- coding: utf-8 -*-
from utility_calculator.database import Database
from utility_calculator.user_data_dir import user_data_dir


db_path = f"{user_data_dir('utility_calculator')}/utility_calculator.db"
database = Database(db_path)

#! usr/bin/python3

import pandas as pd
import numpy as np
from sqlalchemy import Table, select, create_engine

#1
engine = create_engine("mysql://stats:stats@localhost/sakila")
stmt = 'SELECT * FROM rental'
rental = pd.read_sql_query(stmt, engine)


#2 What is the ID number of the staff member who processed the most rentals?
rental['staff_id'].value_counts()[:5].sort_values(ascending=False)
# Output: 1, 8040 and 2: 8004 so staff member 1 processed the most


#3 The table rental tracks the rentals for a store for 3 months in 2005.
# Assuming each customer ID represents a different customer, what is the average number of rentals
# bought by a customer in the 3-month span?
customer_list = rental['customer_id']
np.mean(customer_list.value_counts())
# Output: 26.784641068447414 is average number of rentals bought by a given customer in the three-year span


#4 When an item is rented, how long on average does it take for that item to be returned?
length_of_hold = rental['return_date'] - rental['rental_date']
np.mean(length_of_hold)
# Output: Timedelta('5 days 00:36:28.541706071') On average, it takes just over five days for an
# item to be returned.
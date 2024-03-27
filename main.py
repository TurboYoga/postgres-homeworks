"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
from cvs_reader import CSV_READER


conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='qweh7b3r')

try:
    CSV_READER('employees_data.csv', connect=conn).fill_employees()
    CSV_READER('customers_data.csv', connect=conn).fill_customers()
    CSV_READER('orders_data.csv', connect=conn).fill_orders()
finally:
    conn.close()
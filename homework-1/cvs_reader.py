import csv
import pathlib
import datetime as DT


class CSV_READER():

    def __init__(self, file_name, connect):
        self.path = pathlib.Path(pathlib.Path(__file__).parent, 'north_data', file_name)
        self.conn = connect

    def fill_employees(self):
        with open(self.path, encoding='utf8', newline='') as file:
            data = csv.DictReader(file)

            with self.conn:
                with self.conn.cursor() as cur:
                    for a in data:
                        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                    (int(a['employee_id']), a['first_name'],
                                    a['last_name'], a['title'],
                                    a['birth_date'], a['notes']))


    def fill_customers(self):
        with open(self.path, encoding='utf8', newline='') as file:
            data = csv.DictReader(file)

            with self.conn:
                with self.conn.cursor() as cur:
                    for a in data:
                        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                    (a['customer_id'], a['company_name'], a['contact_name']))



    def fill_orders(self):
        with open(self.path, encoding='utf8', newline='') as file:
            data = csv.DictReader(file)

            with self.conn:
                with self.conn.cursor() as cur:
                    for a in data:
                        date = DT.datetime.strptime(a['order_date'], '%Y-%m-%d').date()
                        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                    (int(a['order_id']),
                                    a['customer_id'], a['employee_id'],
                                     date, a['ship_city']))

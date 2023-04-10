"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2


def read_employees(file):
    with open(file, 'r', encoding='UTF-8') as f:
        data = csv.DictReader(f)
        data_emp = []
        for i in data:
            first_name = i['first_name']
            last_name = i['last_name']
            title = i['title']
            notes = i['notes']
            data_emp.append((first_name, last_name, title, notes))
        return data_emp


def read_customers(file):
    with open(file, 'r', encoding='UTF-8') as f:
        data = csv.DictReader(f)
        data_customers = []
        for i in data:
            customer_id = i['customer_id']
            company_name = i['company_name']
            contact_name = i['contact_name']
            data_customers.append((customer_id, company_name, contact_name))
        return data_customers


def read_orders(file):
    with open(file, 'r', encoding='UTF-8') as f:
        data = csv.DictReader(f)
        data_orders = []
        for i in data:
            order_id = i['order_id']
            customer_id = i['customer_id']
            employee_id = i['employee_id']
            order_data = i['order_date']
            city = i['ship_city']
            data_orders.append((order_id, customer_id, employee_id, order_data, city))
        return data_orders


conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='marinaok481')
try:
    with conn:
        with conn.cursor() as cur:
            data_emp = read_employees('./north_data/employees_data.csv')
            for i in data_emp:
                cur.execute('INSERT INTO employees (first_name, last_name, title, notes) VALUES (%s, %s, %s, %s)', i)
            data_customers = read_customers('./north_data/customers_data.csv')
            for i in data_customers:
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', i)
            data_orders = read_orders('./north_data/orders_data.csv')
            for i in data_orders:
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', i)
finally:
     conn.close()


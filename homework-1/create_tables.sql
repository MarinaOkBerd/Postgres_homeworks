-- SQL-команды для создания таблиц
CREATE TABLE employees(
	employee_id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	notes text NOT NULL
);
SELECT * FROM employees

CREATE TABLE customers(
	customer_id varchar(50) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);
SELECT * FROM customers

CREATE TABLE orders(
	order_id int PRIMARY KEY NOT NULL,
	customer_id varchar(50) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_data date NOT NULL,
	city varchar(100) NOT NULL
);
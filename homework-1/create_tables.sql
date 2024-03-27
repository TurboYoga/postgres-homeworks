-- SQL-команды для создания таблиц


--SELECT * FROM customers;
--SELECT * FROM employees;
--SELECT * FROM orders;
--
--TRUNCATE TABLE employees RESTART IDENTITY CASCADE;
--TRUNCATE TABLE customers RESTART IDENTITY CASCADE;
--TRUNCATE TABLE orders RESTART IDENTITY;


CREATE TABLE if not exists employees
(
	employee_id serial UNIQUE NOT NULL,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title text,
	birth_date varchar(100) NOT NULL,
	notes text
);

CREATE TABLE if not exists customers
(
	customer_id varchar(5) UNIQUE NOT NULL,
	company_name text,
	contact_name text
);

CREATE TABLE if not exists orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(5) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date date NOT NULL,
	ship_city varchar(50)
)
)

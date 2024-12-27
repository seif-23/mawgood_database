Mawgood App Database Manager
Overview
This project provides a Python-based database manager for the "Mawgood App" using PostgreSQL. The DatabaseManager class includes functions for managing and interacting with the application's database, enabling CRUD operations, logging, and user management.

Features
Database Connection Management: Establish and close connections to the PostgreSQL database.
Table Management: List and create database tables.
User Management: Create and verify users with hashed passwords and photos.
Menu Management: Add and delete items from the menu.
Order Management: Insert orders with automatic customer verification and insertion.
Logging: Record user actions in a Logs table.
Requirements
Python 3.x
PostgreSQL
Python libraries:
psycopg2
Tables Schema
Users
username: VARCHAR(250), Primary Key
user_type: VARCHAR(100), NOT NULL
password_hash: TEXT, NOT NULL
user_photo: BYTEA
Customers
email: VARCHAR(250), Primary Key
full_name: VARCHAR(250), NOT NULL
phone_number: VARCHAR(15), NOT NULL
Menu
item_name: VARCHAR(250), Primary Key
type: VARCHAR(100), NOT NULL
image: TEXT
description: TEXT
price: NUMERIC(10, 2), NOT NULL
recipe: TEXT
Orders
order_id: SERIAL, Primary Key
date: DATE, NOT NULL
time: TIME, NOT NULL
username: VARCHAR(250), Foreign Key → Users(username)
email: VARCHAR(250), Foreign Key → Customers(email)
price: NUMERIC(10, 2), NOT NULL
tip: NUMERIC(10, 2)
offer: NUMERIC(10, 2)
total: NUMERIC(10, 2), NOT NULL
notes: TEXT
items: JSONB, NOT NULL
Logs
date: DATE, NOT NULL
time: TIME, NOT NULL
username: VARCHAR(250), Foreign Key → Users(username)
action: TEXT, NOT NULL
Error Handling
The functions handle common errors such as duplicate entries or missing data by returning descriptive error messages.

Notes
Ensure your PostgreSQL server is configured to accept connections from the host where this script runs.
Use a strong, hashed password for password_hash when creating users.
Adapt the schema and functionality as required for your application

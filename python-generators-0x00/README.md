# Python Generators

## 0. Getting started with python generators

### Objective

create a generator that streams rows from an SQL database one by one.

### Instructions

Write a python script that `seed.py`:

1. Set up the MySQL database, `ALX_prodev` with the table user_data with the following fields:
    - `user_id(Primary Key, UUID, Indexed)`
    - `name (VARCHAR, NOT NULL)`
    - `email (VARCHAR, NOT NULL)`
    - `age (DECIMAL,NOT NULL)`
2. Populate the database with the sample data from this `user_data.csv`
3. Prototypes:
    - `def connect_db()` :- connects to the mysql database server
    - `def create_database(connection)`:- creates the database `ALX_prodev` if it does not exist
    - `def connect_to_prodev()` connects the the `ALX_prodev` database in MYSQL
    - `def create_table(connection)`:- creates a table user_data if it does not exists with the required fields
    - `def insert_data(connection, data)`:- inserts data in the database if it does not exist

## 1. generator that streams rows from an SQL database

### Objective

create a generator that streams rows from an SQL database one by one

### Instructions

In `0-stream_users.py` write a function that uses a generator to fetch rows one by one from the `user_data` table. You must use the `Yield` python generator

- Prototype: `def stream_users()`
- Your function should have no more than 1 loop

## 2. Batch processing Large Data

### Objective

Create a generator to fetch and process data in batches from the users database

### Instructions

1. Write a function stream_users_in_batches(batch_size) that fetches rows in batches

2. Write a function batch_processing() that processes each batch to filter users over the age of25`

3. You must use no more than 3 loops in your code. Your script must use the yield generator

    - def stream_users_in_batches(batch_size)
    - def batch_processing(batch_size)

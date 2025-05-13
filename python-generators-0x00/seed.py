#!/usr/bin/python3
# seed.py
import csv
import mysql.connector

def connect_to_db():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root')
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    try:
        cursor = connection.cursor()
        # Create a new database
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def connect_to_prodev():
    try:
        # Connect to the ALX_prodev database
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            database='ALX_prodev')
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    table = f"CREATE TABLE IF NOT EXISTS  user_data\
        (user_id UUID PRIMARY KEY,\
        name VARCHAR NOT NULL,\
        email VARCHAR NOT NULL,\
        age DECIMAL NOT NULL)\
    "
    try:
        cursor = connection.cursor()
        # Create a new table
        cursor.execute(table)
        print("Table created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_data(connection, data):
    """insert data from csv file"""
    try:
        cursor = connection.cursor()
        # Insert data into the table
        insert_query = "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)"
        with open(data, 'r') as file:
            csv_reader = csv.reader(file)
            row = next(csv_reader)
            for row in csv_reader:
                cursor.execute(insert_query, row)
        connection.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

#!/usr/bin/python3
import mysql.connector


def stream_users():
    """Generator connecting to the database and yielding rows from the users table.
        Yields:
            tuple: A row from the users table.
    """
    try:
        db = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="ALX_prodev",
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        db.close()

#!/usr/bin/python3
seed = __import__('seed')


def stream_users():
    """Generator connecting to the database and yielding rows from the users table.
    Yields:
        dict: A row from the user_data table.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    connection.close()

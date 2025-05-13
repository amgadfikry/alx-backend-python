#!/usr/bin/python3
seed = __import__('seed')


def paginate_users(page_size, offset):
    """Fetches a page of user data from the user_data table.
    Args:
        page_size (int): Number of rows to fetch per page.
        offset (int): Offset for pagination.
    Yields:
        list of dict: A page of user rows.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """Generator that lazily paginates through user_data table.
    Args:
        page_size (int): Number of rows to fetch per page.
    Yields:
        list of dict: A page of user rows.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size

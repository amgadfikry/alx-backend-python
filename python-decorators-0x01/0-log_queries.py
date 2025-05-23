#!/usr/bin/env python3
import functools

def log_queries(func):
    """
    Decorator to log SQL queries executed by the function.
    This decorator wraps the function and prints the SQL query
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        if query:
            print(f"[SQL LOG] Executing query: {query}")
        else:
            print("[SQL LOG] No SQL query found")
        return func(*args, **kwargs)
    return wrapper

import time
import logging
from django.db import connection, reset_queries
from functools import wraps

logger = logging.getLogger(__name__)
def find_be_url(environment=None):
    """
    Returns the url based on the environment
    if environment is dev then return https://dev.com/api/
    if environment is stage then return https://stage.com/api/
    if local then return http://127.0.0.1:8000/api/
    """
    if environment == "dev":
        return "https://dev.com/api/"
    elif environment == "stage":
        return "https://stage.com/api/"
    else:
        return "http://127.0.0.1:8000/api/"
    
def find_fe_url(environment=None):
    """
    Returns the url based on the environment
    if environment is dev then return https://dev.com/
    if environment is stage then return https://stage.com/
    if local then return http://127.0.0.1:8000/
    """
    if environment == "dev":
        return "https://dev.com/"
    elif environment == "stage":
        return "https://stage.com/"
    else:
        return "http://127.0.0.1:8001/silk/"
    



def log_query_count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        reset_queries()
        start_queries = len(connection.queries)
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        end_queries = len(connection.queries)
        total_queries = end_queries - start_queries
        execution_time = end_time - start_time

        print(
            f"Function `{func.__name__}` executed {total_queries} queries in {execution_time:.2f}s"
        )

        return result
    return wrapper
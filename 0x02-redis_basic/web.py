#!/usr/bin/env python3
"""Module to obtain HTML content of a particular URL and return it."""

import redis
import requests
from functools import wraps

redis_client = redis.Redis()


def cache_page(method):
    """
    Decorator that caches result of the get_page function.
    Tracks access count in Redis & caches results for 10 seconds.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function for the method."""
        cache_key = "cached:" + url
        count_key = "count:" + url
        redis_client.incr(count_key)

        cached_result = redis_client.get(cache_key)
        if cached_result:
            return cached_result.decode('utf-8')

        result = method(url)
        redis_client.setex(cache_key, 10, result)

        return result
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """
    Gets HTML content of a URL.

    Args:
        url (str): the URL to fetch.

    Returns:
        str: the HTML content of the URL.
    """
    response = requests.get(url)
    return response.text

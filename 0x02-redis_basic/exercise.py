#!/usr/bin/env python3
"""Module to store an instance of the Redis client as specced."""

import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count calls to the method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Calls original method w/ provided arguments and-
        -returns its result.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    Cache class that interacts with Redis.
    """
    def __init__(self) -> None:
        """
        The constructor method for Cache instances.

        It sets up the Redis client, and flushing all existing keys-
        -to make sure the database is empty.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key & stores the input data in-
        -Redis using the random key.

        Args:
            data (Union[str, bytes, int, float]): data to be stored.

        Returns:
            str: the generated key for the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[
        [bytes],
        Union[str, int, float, bytes]
    ]] = None) -> Optional[Union[str, int, float, bytes]]:
        """
        Gets data from Redis and applies anoptional conversion function.

        Args:
            key (str): the key to retrieve data for.
            fn: function to convert data from bytes to desired type.

        Returns:
            Optional: the retrieved data, converted if `fn` is provided-
            -or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """
        Gets a string from Redis w/ utf-8 decoding.

        Args:
            key (str): the key to get data for.

        Returns:
            Optional[str]: the retrieved string data-
            -or None if the key doesn't exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Gets an integer from Redis, assuming the stored data is numeric.

        Args:
            key (str): The key to retrieve data for.

        Returns:
            Optional[int]: The retrieved integer data or-
            -None if the key does not exist.
        """
        return self.get(key, fn=int)

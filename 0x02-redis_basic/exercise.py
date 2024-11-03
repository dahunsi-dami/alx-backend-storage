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


def call_history(method: Callable) -> Callable:
    """
    Decorator to store history of inputs and outputs-
    -of the decorated function.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Creates keys for input and output history.
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)

        return output
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
    @call_history
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


def replay(method: Callable) -> None:
    """
    Displays history of calls for the method that's passed.

    Args:
        method (Callable): the method to replay history for.
    """
    cache = method.__self__
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)
    count = len(inputs)

    print(f"{method.__qualname__} was called {count} times:")
    for inp, out in zip(inputs, outputs):
        print(
            f"{method.__qualname__}(*{eval(inp.decode('utf-8'))}) -> "
            f"{out.decode('utf-8')}"
        )

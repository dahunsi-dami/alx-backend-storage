#!/usr/bin/env python3
"""Module to store an instance of the Redis client as specced."""

import redis
import uuid
from typing import Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key & stores the input data in-
        -Redis using the random key.

        Args:
            data (Union[str, bytes, int, float]): data to be stored.

        Returns:
            str: the generated key for the stored data.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

#!/usr/bin/env python3
"""Redis Basis.

This module contains the learning requirement for redis in python.
"""
import uuid
from typing import Union
import redis


class Cache:
    """
    Cache class

    store(self, data): Stores data in a redis database
    """

    def __init__(self) -> None:
        """Entry Point"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in a redis database

        Args:
            data (Union[str, bytes, int, float]): The data to be stored
        Return:
            str: Key
        """
        key: str = uuid.uuid4().hex
        self._redis.set(key, data)
        return key

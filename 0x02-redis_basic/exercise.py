#!/usr/bin/env python3
"""Redis Basis.

This module contains the learning requirement for redis in python.
"""
import functools
import uuid
from typing import Any, Callable, Union
import redis


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of calls made to a method
    and store the count in Redis.

    Args:
      method (Callable): The method to be decorated.

    Returns:
      Callable: A wrapper function that calls the decorated method
            and increments a Redis counter associated with the
            method's qualified name.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to track the input arguments and return values
        of method calls using Redis lists.

    Args:
      method (Callable): The method to be decorated.

    Returns:
      Callable: A wrapper function that calls the decorated method,
                stores the input arguments and return value in separate
                Redis lists, and then returns the method's result.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        res = method(self, *args, **kwargs)

        redis.Redis().rpush(method.__qualname__ + ":input", str(args))
        redis.Redis().rpush(method.__qualname__ + ":output", res)

    return wrapper


class Cache:
    """
    Cache class

    store(self, data): Stores data in a redis database
    """

    def __init__(self) -> None:
        """Entry Point"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in a redis database

        Args:
            data (Union[str, bytes, int, float]): The data to be stored
        Returns:
            str: Key
        """
        key: str = uuid.uuid4().hex
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable) -> Any:
        """
        Retrieves data from Redis for a given key and optionally applies
        a transformation function.

        Params:
          self (RedisWrapper): An instance of the RedisWrapper class.
          key (str): The key to retrieve data for from the Redis store.
          fn (Callable[[str], Any], optional): A callable function to be
                  applied to the retrieved data (if provided).
                  The function should accept a string argument.

        Returns:
          Any: The retrieved data from Redis (as bytes) if no
              transformation function is provided.
               The result of applying the transformation function `fn`
               to the decoded string data (if provided).

        Raises:
          pyredis.exceptions.RedisError: If an error occurs
            while interacting with the Redis server.
        """
        data = self._redis.get(key)
        if fn is None:
            return data
        return fn(str)

    def get_str(self, key: str) -> str:
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        return self.get(key, int)

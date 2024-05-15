#!/usr/bin/env python3
""" Tracker callls """

import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """ Decorator to know the number of calls """

    @wraps(method)
    def wrapper(url):
        """ Wrapper decorator """
        r.incr(f"count:{url}")
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """ Get page
    """
    req = requests.get(url)
    return req.text

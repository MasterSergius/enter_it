import json
import time
from functools import wraps


def make_cache_key(func, *args, **kwargs) -> str:
    args_str = ";".join((str(arg) for arg in args))
    kwargs_str = ";".join(f"{k}:{v}" for k, v in kwargs.items())
    cache_key = f"{func.__name__}-{args_str}-{kwargs_str}"
    return cache_key


def read_cache(disk_cache_path) -> dict[str, dict]:
    try:
        with open(disk_cache_path, "r") as f:
            cache_data = json.load(f)
        return cache_data
    except Exception:
        return {}


def get_from_cache(disk_cache_path, cache_key):
    cache_data = read_cache(disk_cache_path)
    if cache_entry := cache_data.get(cache_key):
        if cache_entry["expiration"] < time.time():
            del cache_data[cache_key]
        else:
            return cache_data[cache_key]["data"]
    return None


def add_to_cache(disk_cache_path, cache_key, data, ttl):
    cache_data = read_cache(disk_cache_path)
    cache_data[cache_key] = {"data": data, "expiration": int(time.time()+ttl)}
    with open(disk_cache_path, "w") as f:
        cache_data = json.dump(cache_data, f)


def ttl_disk_cache(disk_cache_path, ttl=3600):
    def wrapper(func):
        @wraps(func)
        def result(*args, **kwargs):
            cache_key = make_cache_key(func, *args, **kwargs)
            if not (wrapped_result := get_from_cache(disk_cache_path, cache_key)):
                wrapped_result = func(*args, **kwargs)
                add_to_cache(disk_cache_path, cache_key, wrapped_result, ttl)
            return wrapped_result
        return result
    return wrapper

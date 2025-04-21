import os
import time
from freezegun import freeze_time
from ttl_cache import add_to_cache
from ttl_cache import get_from_cache
from ttl_cache import make_cache_key
from ttl_cache import read_cache
from ttl_cache import ttl_disk_cache


freezer = freeze_time("2000-01-01 00:00:00")


def func_for_testing(*args, **kwargs):
    return f"called with {args} and {kwargs}"


def test_make_cache_key():
    expected = "func_for_testing--"
    actual = make_cache_key(func_for_testing)
    assert actual == expected

    expected = "func_for_testing-1-"
    actual = make_cache_key(func_for_testing, "1")
    assert actual == expected

    expected = "func_for_testing-1;2-"
    actual = make_cache_key(func_for_testing, "1", "2")
    assert actual == expected

    expected = "func_for_testing-1;2-a:3"
    actual = make_cache_key(func_for_testing, "1", "2", a="3")
    assert actual == expected


def test_add_and_get_from_cache():
    freezer.start()
    disk_cache_path = "test_add_and_get_from_cache.json"
    add_to_cache(disk_cache_path, "test_key", {"a": 1}, 3600)
    try:
        assert read_cache(disk_cache_path) == {'test_key': {'data': {'a': 1}, 'expiration': 946688400}}
        assert get_from_cache(disk_cache_path, "test_key") == {'a': 1}
        assert get_from_cache(disk_cache_path, "test_key2") is None
    except Exception as exc:
        raise Exception from exc
    finally:
        os.remove(disk_cache_path)
        freezer.stop()


def test_ttl_disk_cache():
    freezer.start()
    disk_cache_path = "test_add_and_get_from_cache.json"
    wrapped_func = ttl_disk_cache(disk_cache_path, 3600)(func_for_testing)
    assert read_cache(disk_cache_path) == {}
    try:
        wrapped_func("hello")
        assert read_cache(disk_cache_path) == {
            'func_for_testing-hello-': {
                'data': "called with ('hello',) and {}",
                'expiration': 946688400,
            }
        }
    except Exception as exc:
        raise Exception from exc
    finally:
        os.remove(disk_cache_path)
        freezer.stop()


def test_expiration():
    disk_cache_path = "test_add_and_get_from_cache.json"
    wrapped_func = ttl_disk_cache(disk_cache_path, 1)(func_for_testing)
    assert read_cache(disk_cache_path) == {}
    try:
        wrapped_func("hello")
        assert get_from_cache(disk_cache_path, "func_for_testing-hello-") == "called with ('hello',) and {}"
        # wait for expiration
        time.sleep(2)
        assert get_from_cache(disk_cache_path, "func_for_testing-hello-") is None
    except Exception as exc:
        raise Exception from exc
    finally:
        os.remove(disk_cache_path)

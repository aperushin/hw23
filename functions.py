from typing import Iterable


def filter_query(data: Iterable, param: str):
    return filter(lambda line: param in line, data)


def map_query(data: Iterable, param: str):
    return map(lambda line: line.split()[int(param)], data)


def unique_query(data: Iterable, *args, **kwargs):
    return set(data)


def sort_query(data: Iterable, param: str):
    return sorted(data, reverse=True if param == 'desc' else False)


def limit_query(data: Iterable, param: str):
    return list(data)[:int(param)]

from typing import Iterable
import re


def filter_query(data: Iterable[str], param: str) -> filter:
    return filter(lambda line: param in line, data)


def map_query(data: Iterable[str], param: str) -> map:
    return map(lambda line: line.split()[int(param)], data)


def unique_query(data: Iterable[str], *args, **kwargs) -> set[str]:
    return set(data)


def sort_query(data: Iterable[str], param: str) -> list[str]:
    return sorted(data, reverse=True if param == 'desc' else False)


def limit_query(data: Iterable[str], param: str) -> list[str]:
    return list(data)[:int(param)]


def regex(data: Iterable[str], param: str) -> filter:
    expression = re.compile(param)
    return filter(lambda line: expression.search(line), data)

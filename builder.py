from typing import Generator, Callable
from functions import filter_query, map_query, unique_query, sort_query, limit_query, regex
from constants import DATA_DIR

CMD_TO_FUNCTION: dict[str, Callable] = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
    'regex': regex
}


def iter_file(filename: str) -> Generator[str, None, None]:
    with open(filename, encoding='utf-8') as f:
        for line in f:
            yield line


def build_query(cmd: dict) -> list[str]:
    data = iter_file(DATA_DIR + cmd['file_name'])
    result = CMD_TO_FUNCTION[cmd['cmd1']](data=data, param=cmd['value1'])
    result = CMD_TO_FUNCTION[cmd['cmd2']](data=result, param=cmd['value2'])
    return list(result)

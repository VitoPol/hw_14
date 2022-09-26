from re import search
from req import *


def parse_str(text: str) -> tuple:
    """
    Проверяет корректность запроса и разбивает его на отдельные элементы
    :param text: запрос
    :return: кортеж с запросами и их параметрами
    """
    correct_queries = ["filter", "map", "unique", "sort", "limit"]
    queries = search(r"^(\S+) (\S+) \| (\S+) (\S+)$", text)
    if queries:
        if queries[1] in correct_queries and queries[3] in correct_queries:
            return queries[1], queries[2], queries[3], queries[4]
    return None, None, None, None


def read_file() -> list:
    """
    :return: список строк из файла
    """
    with open("./data/apache_logs.txt") as file:
        content = file.read()
    return content.strip().split("\n")


def execute_query(logs_lines: Iterator, query: str, param: str) -> Iterator:
    if query == "filter":
        return filter(lambda s: param in s, logs_lines)
    elif query == "map":
        return q_map(logs_lines, param)
    elif query == "unique" and param == "-":
        return q_unique(logs_lines)
    elif query == "sort":
        return q_sort(logs_lines, param)
    elif query == "limit":
        return q_limit(logs_lines, param)
    else:
        return logs_lines


def main() -> None:
    logs_lines = iter(read_file())
    query = input(">>> ")
    query1, param1, query2, param2 = parse_str(query)
    if not query1:
        return None
    logs_lines = execute_query(logs_lines, query1, param1)
    logs_lines = execute_query(logs_lines, query2, param2)
    [print(line) for line in list(logs_lines)]


if __name__ == "__main__":
    main()


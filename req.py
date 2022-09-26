from typing import Iterator


def q_map(logs: Iterator, param: str) -> Iterator:
    """
    Итератор возвращающий нужный столбец
    :param logs: входной итератор
    :param param: номер столбца
    :return: итератор по столбцу
    """
    for line in logs:
        try:
            yield line.split()[int(param)]
        except:
            continue


def q_unique(logs: Iterator) -> Iterator:
    """
    итератор оставляющий только уникальные строки
    :param logs: входной итератор
    :return: итератор уникальных строк
    """
    logs = iter(set(logs))
    for line in logs:
        yield line


def q_sort(logs: Iterator, param: str) -> Iterator:
    """
    итератор сортировки
    :param logs: входной итератор
    :param param: строка 'asc' для сортировки по возрастанию или 'desc' для обратной сортировки
    :return:
    """
    if param == "asc":
        return iter(sorted(logs))
    elif param == "desc":
        return iter(sorted(logs, reverse=True))
    else:
        return logs


def q_limit(logs: Iterator, param: str) -> Iterator:
    """
    итератор ограничивающий кол-во выводимых строк
    :param logs: входной итератор
    :param param: кол-во строк
    :return: итератор из нужного кол-ва строк
    """
    for _ in range(int(param)):
        try:
            yield logs.__next__()
        except StopIteration:
            break

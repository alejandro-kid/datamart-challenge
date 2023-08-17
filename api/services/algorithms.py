from flask import Response
from heapq import merge

def merge_array_endpoint() -> Response:
    pass


def merge_array(list_1: list, list_2: list) -> list:
    return list(merge(list_1, list_2))
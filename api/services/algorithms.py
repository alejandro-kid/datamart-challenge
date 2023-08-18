
import multiprocessing

from config.gunicorn import workers
from heapq import merge


def merge_array(list_1: list, list_2: list) -> list:
    return list(merge(list_1, list_2))


def is_sorted(number_list: list) -> bool:
    return all(a <= b for a, b in zip(number_list, number_list[1:]))


def binary_search(ordered_list: list, element) -> bool:

  if len(ordered_list) == 0:
    return False

  medio = len(ordered_list) // 2
  if ordered_list[medio] == element:
    return True
  elif ordered_list[medio] > element:
    return binary_search(ordered_list[:medio], element)
  else:
    return binary_search(ordered_list[medio + 1:], element)

def map_function(list_1: list, list_2) -> dict:
    return dict(map(
        lambda elemento: (elemento, binary_search(list_1, elemento)), list_2
        ))


def map_function_workers(list_1: list, list_2: list) -> dict:

    pool = multiprocessing.Pool(workers)

    results = pool.starmap(binary_search,
                           [(list_1, elemento) for elemento in list_2])

    mapping_dict = {
        list_2[index]: element for index, element in enumerate(results)
    }

    pool.close()
    pool.join()

    return mapping_dict

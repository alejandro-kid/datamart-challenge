
import multiprocessing

from config.gunicorn import workers

def binary_insertion_sort_merge(list_1: list, list_2: list) -> tuple:
  merged_list = tuple(list_1 + list_2)
  for i in range(1, len(merged_list)):
      key = merged_list[i]
      left = 0
      right = i - 1
      while left <= right:
          mid = (left + right) // 2
          if merged_list[mid] > key:
              right = mid - 1
          else:
              left = mid + 1
      merged_list = merged_list[:left] + (key,) + merged_list[left:i] + \
                    merged_list[i+1:]
  return merged_list

def median(list_1: list) -> float:
  if ( not is_sorted(list_1)):
    list_1.sort()

  n = len(list_1)
  if n % 2 == 1:
    return list_1[n // 2]
  else:
    return (list_1[n // 2] + list_1[n // 2 - 1]) / 2

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

from api.services.algorithms import map_function, map_function_workers

def test_map_function_list() -> None:
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [6, 7, 8, 3, 10]
    diccionario = map_function(list_1, list_2,)

    assert diccionario == {6: False, 7: False, 8: False, 3: True, 10: False}

def test_map_function_list_workers() -> None:
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [6, 7, 8, 3, 10]
    diccionario = map_function_workers(list_1, list_2,)

    assert diccionario == {6: False, 7: False, 8: False, 3: True, 10: False}

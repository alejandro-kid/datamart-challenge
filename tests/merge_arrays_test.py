import json
import jsonschema
import pytest

from api.services.algorithms import merge_array
from api.schemas.merge_arrays_schema import merge_arrays_schema
from hypothesis import given
from hypothesis.strategies import lists, integers, text, booleans, floats
from tests.conftest import helper

ordered_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
ordered_2 = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
unordered = (5, 12, 1, 8, 7, 3, 9, 6, 10, 4)

def test_merge_arrays() -> None:

    mixed_ordered_list = merge_array(ordered_1, ordered_2)
    assert mixed_ordered_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                  13, 14, 15, 16, 17, 18, 19, 20]

def test_merge_arrays_endpoint(client) -> None:

    response = client.post('/merge_arrays', data=json.dumps(dict(
    list_1=ordered_1,
    list_2=ordered_2
    )), mimetype='application/json')
    
    response_info = helper(response.response)


    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response_info["message"] == "Successfully merged list"
    assert response_info["success"] is True
    assert response_info["mixed_ordered_list"] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                                   12, 13, 14, 15, 16, 17, 18, 19, 20]


def test_merge_arrays_endpoint_with_unordered_list(client):

    response = client.post('/merge_arrays', data=json.dumps(dict(
    list_1=unordered,
    list_2=ordered_2
    )), mimetype='application/json')
    
    response_info = helper(response.response)


    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response_info["message"] == "Successfully merged list"
    assert response_info["success"] is True
    assert response_info["mixed_ordered_list"] == [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                                   12, 13, 14, 15, 16, 17, 18, 19, 20]


@given(lists(elements=integers(min_value=1, max_value=100), min_size=1, max_size=20),
       lists(elements=integers(min_value=1, max_value=100), min_size=1, max_size=20))
def test_merge_arrays_schema_good_way(list_1: list, list_2: list) -> None:

    td_post_body = {
        "list_1": list_1,
        "list_2": list_2,
    }

    assert isinstance(list_1, list)
    assert all(isinstance(element, int) for element in list_1)
    assert isinstance(list_2, list)
    assert all(isinstance(element, int) for element in list_2)
    jsonschema.validate(td_post_body, merge_arrays_schema)


@pytest.mark.xfail
@given(list_1=lists(floats(), min_size=1, max_size=20),
       list_2=lists(text(), min_size=1, max_size=20),
       list_3=lists(booleans(), min_size=1, max_size=20),
       list_4=lists(integers(), min_size=1, max_size=20))
def test_merge_arrays_schema_mixed_list(list_1: list, list_2: list,
                                       list_3: list, list_4: list) -> None:

    td_post_body_variant_1 = {
        "list_1": list_1,
        "list_2": list_2,
    }

    td_post_body_variant_2 = {
        "list_1": list_1,
        "list_2": list_3,
    }

    td_post_body_variant_3 = {
        "list_1": list_1,
        "list_2": list_4,
    }
    assert isinstance(list_1, list)
    assert isinstance(list_2, list)
    assert isinstance(list_3, list)
    assert isinstance(list_4, list)
    jsonschema.validate(td_post_body_variant_1, merge_arrays_schema)
    jsonschema.validate(td_post_body_variant_2, merge_arrays_schema)
    jsonschema.validate(td_post_body_variant_3, merge_arrays_schema)

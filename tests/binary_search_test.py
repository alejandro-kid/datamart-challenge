import json
import jsonschema
import pytest

from api.services.algorithms import binary_search
from api.schemas.binary_search_schema import binary_search_schema
from hypothesis import given
from hypothesis.strategies import lists, integers, floats, text
from tests.conftest import helper

number_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def test_binary_search_endpoint(client) -> None:

    response = client.post('/binary_search', data=json.dumps(dict(
        ordered_list=number_list,
        element=9
    )), mimetype='application/json')
    
    response_info = helper(response.response)

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response_info["message"] == "Successfully searched"
    assert response_info["success"] is True
    assert response_info["found"] is True


def test_number_found():
        ordered_list = [1, 3, 5, 7, 9]
        element = 5

        assert binary_search(ordered_list, element)

def test_number_not_found_smaller():
    ordered_list = [1, 3, 5, 7, 9]
    element = 0

    assert binary_search(ordered_list, element) is not True

def test_number_not_found_greater():
    ordered_list = [1, 3, 5, 7, 9]
    element = 10

    assert binary_search(ordered_list, element) is not True

@given(lists(elements=integers(), min_size=1, max_size=20),
       integers())
def test_binary_search_schema(ordered_list: list, element) -> None:

    td_post_body = {
        "ordered_list": ordered_list,
        "element": element
    }

    jsonschema.validate(td_post_body, binary_search_schema)

@pytest.mark.xfail
@given(lists(elements=text(), min_size=1, max_size=20),
       text())
def test_binary_search_schema_not_number(ordered_list: list, element) -> None:

    td_post_body = {
        "ordered_list": ordered_list,
        "element": element
    }

    jsonschema.validate(td_post_body, binary_search_schema)
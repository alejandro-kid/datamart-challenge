import json
import jsonschema
import pytest
import statistics

from api.schemas.median_schema import median_schema
from api.services.algorithms import median
from hypothesis import given
from hypothesis.strategies import lists, integers, floats, text
from tests.conftest import helper

number_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def test_median_endpoint(client) -> None:

    response = client.post('/median', data=json.dumps(dict(
    list=number_list,
    )), mimetype='application/json')
    
    response_info = helper(response.response)


    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response_info["message"] == "Successfully calc"
    assert response_info["success"] is True
    assert response_info["median"] == 5.5


@given(lists(elements=integers(), min_size=1, max_size=20))
def test_median_schema_for_integer(number_list: list) -> None:

    td_post_body = {
        "list": number_list,
    }

    assert isinstance(number_list, list)
    jsonschema.validate(td_post_body, median_schema)


@given(lists(elements=floats(), min_size=1, max_size=20))
def test_median_schema_for_floats(number_list: list) -> None:

    td_post_body = {
        "list": number_list,
    }

    assert isinstance(number_list, list)
    jsonschema.validate(td_post_body, median_schema)


@pytest.mark.xfail
@given(lists(elements=text(), min_size=1, max_size=20))
def test_median_schema_for_not_number(not_number_list: list) -> None:

    td_post_body = {
        "list": not_number_list,
    }

    assert isinstance(number_list, list)
    assert all(isinstance(element, int) for element in number_list)
    jsonschema.validate(td_post_body, median_schema)

@given(lists(elements=integers(), min_size=1, max_size=20))
def test_median_algorithm_integer(number_list: list) -> None:
    assert median(number_list) == statistics.median(number_list)


@given(lists(elements=floats(allow_nan=False, allow_infinity=False),
            min_size=1, max_size=20))
def test_median_algorithm_float(number_list: list) -> None:
    assert median(number_list) == statistics.median(number_list)
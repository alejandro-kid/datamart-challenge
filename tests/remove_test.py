import json
import jsonschema
import pytest

from api.schemas.remove_duplicates import remove_duplicates_schema
from hypothesis import given
from hypothesis.strategies import lists, integers, text
from tests.conftest import helper

number_list = [8, 1, 2, 3, 4, 5, 3, 6, 7, 2, 8, 8, 8, 9, 10]

def test_remove_duplicates_endpoint(client) -> None:

    response = client.post('/remove_duplicates', data=json.dumps(dict(
    list=number_list,
    )), mimetype='application/json')
    
    response_info = helper(response.response)


    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response_info["message"] == "Successfully clean"
    assert response_info["success"] is True
    assert response_info["filtered_list"] == list(set(number_list))


@given(lists(text(), min_size=1, max_size=20))
def test_remove_duplicates_schema(number_list: list) -> None:

    td_post_body = {
        "list": number_list,
    }

    assert isinstance(number_list, list)
    jsonschema.validate(td_post_body, remove_duplicates_schema)


@pytest.mark.xfail
@given(integers())
def test_remove_duplicates_schema_not_list(not_list: any) -> None:

    td_post_body = {
        "list": not_list,
    }

    assert isinstance(number_list, list)
    jsonschema.validate(td_post_body, remove_duplicates_schema)
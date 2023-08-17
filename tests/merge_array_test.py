import json

from api.services.algorithms import merge_array
from tests.conftest import helper

ordered_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
ordered_2 = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
unordered = (5, 12, 1, 8, 7, 3, 9, 6, 10, 4)

def test_merge_array() -> None:

    mixed_ordered_list = merge_array(ordered_1, ordered_2)
    assert mixed_ordered_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                  13, 14, 15, 16, 17, 18, 19, 20]

def test_merge_array_endpoint(client) -> None:

    response = client.post('/merge_array', data=json.dumps(dict(
    lista_1=ordered_1,
    lista_2=ordered_2
    )), mimetype='application/json')
    
    response_info = helper(response.response)


    assert response.status_code == 201
    assert response.content_type == 'application/json'
    assert response_info["message"] == "Successfully merged list"
    assert response_info["success"] is True
    assert response_info["mixed_ordered_list"] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                                   12, 13, 14, 15, 16, 17, 18, 19, 20]


def test_merge_array_endpoint_with_unordered_list(client):

    response = client.post('/merge_array', data=json.dumps(dict(
    lista_1=unordered,
    lista_2=ordered_2
    )), mimetype='application/json')
    
    response_info = helper(response.response)


    assert response.status_code == 201
    assert response.content_type == 'application/json'
    assert response_info["message"] == "Successfully merged list"
    assert response_info["success"] is True
    assert response_info["mixed_ordered_list"] == [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                                   13, 14, 15, 16, 17, 18, 19, 20]

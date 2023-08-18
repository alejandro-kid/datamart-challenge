import jsonschema
import statistics

from api.schemas.merge_arrays_schema import merge_arrays_schema
from api.schemas.median_schema import median_schema
from flask import Response, request, json
from heapq import merge


def merge_arrays_endpoint() -> Response:
    try:
        request_data = request.get_json()
        jsonschema.validate(request_data, merge_arrays_schema)

        list_1 = request_data["list_1"]
        list_2 = request_data["list_2"]

        if not is_sorted(list_1):
            list_1 = sorted(list_1)

        if not is_sorted(list_2):
            list_2 = sorted(list_1)

        mixed_ordered_list = merge_array(list_1, list_2)

        data = {
            "success": True,
            "message": "Successfully merged list",
            "mixed_ordered_list": mixed_ordered_list
        }
        response = Response(json.dumps(data), 200, mimetype="application/json")

    except jsonschema.exceptions.ValidationError as exc:
        response = Response(str(exc.message), 400, mimetype="application/json")
    except Exception as e:
        data = {
            "success": False,
            "error_message": str(e)
        }
        response = Response(json.dumps(data), 500, mimetype='application/json')

    return response


def merge_array(list_1: list, list_2: list) -> list:
    return list(merge(list_1, list_2))


def is_sorted(number_list: list) -> bool:
    return all(a <= b for a, b in zip(number_list, number_list[1:]))


def find_median_endpoint() -> Response:
    try:
        request_data = request.get_json()
        jsonschema.validate(request_data, median_schema)

        number_list = request_data["list"]

        median = statistics.median(number_list)

        data = {
            "success": True,
            "message": "Successfully calc",
            "median": median
        }
        response = Response(json.dumps(data), 200, mimetype="application/json")

    except jsonschema.exceptions.ValidationError as exc:
        response = Response(str(exc.message), 400, mimetype="application/json")
    except Exception as e:
        data = {
            "success": False,
            "error_message": str(e)
        }
        response = Response(json.dumps(data), 500, mimetype='application/json')

    return response

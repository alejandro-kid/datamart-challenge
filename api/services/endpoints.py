
import jsonschema

from api.schemas.merge_arrays_schema import merge_arrays_schema
from api.schemas.median_schema import median_schema
from api.schemas.remove_duplicates import remove_duplicates_schema
from api.services.algorithms import binary_insertion_sort_merge
from api.services.algorithms import is_sorted, binary_search, median
from flask import Response, request, json


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

        mixed_ordered_list = binary_insertion_sort_merge(list_1, list_2)

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


def find_median_endpoint() -> Response:
    try:
        request_data = request.get_json()
        jsonschema.validate(request_data, median_schema)

        number_list = request_data["list"]

        median_list = median(number_list)

        data = {
            "success": True,
            "message": "Successfully calc",
            "median": median_list
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


def remove_duplicates_endpoint() -> Response:
    try:
        request_data = request.get_json()
        jsonschema.validate(request_data, remove_duplicates_schema)

        dirty_list = request_data["list"]

        filtered_list = set(dirty_list)

        data = {
            "success": True,
            "message": "Successfully clean",
            "filtered_list": list(filtered_list)
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


def binary_search_endpoint() -> Response:
    try:
        request_data = request.get_json()
        jsonschema.validate(request_data, merge_arrays_schema)

        ordered_list = request_data["ordered_list"]
        element = request_data["element"]

        if not is_sorted(ordered_list):
            ordered_list = sorted(ordered_list)

        found = binary_search(ordered_list, element)

        data = {
            "success": True,
            "message": "Successfully searched",
            "found": found
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
binary_search_schema = {
    "type": "object",
    "properties": {
        "ordered_list": {
            "type": "array",
            "items": {"type": "number"}
        },
        "element": {
            "type": "number"
            }
    },
    "requiered": ["ordered_list", "element"]
}

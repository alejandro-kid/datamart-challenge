merge_arrays_schema = {
    "type": "object",
    "properties": {
        "list_1": {
            "type": "array",
            "items": {"type": "integer"}
        },
        "list_2": {
            "type": "array",
            "items": {"type": "integer"}
            }
    },
    "requiered": ["list_1", "list_2"]
}

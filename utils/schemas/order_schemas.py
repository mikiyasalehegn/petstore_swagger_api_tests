GET_STORE_INVENTORY_SCHEMA = {
    "type": "object",
    "properties": {
        "sold": {"type": "integer"},
        "available": {"type": "integer"},
        "invalid_status": {"type": "integer"},
        "pending": {"type": "integer"},
        "peric": {"type": "integer"},
    },
    "required": ["sold", "available", "pending"]
}

PLACE_ORDER_PET_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "petId": {"type": "integer"},
        "quantity": {"type": "integer"},
        "shipDate": {"type": "string"},
        "status": {"type": "string"},
        "complete": {"type": "boolean"},
    },
        "required": ["id", "petId", "quantity", "shipDate", "status"]

}


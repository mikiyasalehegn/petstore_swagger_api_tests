get_pet_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "status": {"type": "string"},
    },
    "required": ["id", "name", "status"]
}

error_message = {
  "type": "object",
  "properties": {
      "code": "integer",
      "type": "string",
      "message": "string"
  },
  "required": ["code", "message"]
}





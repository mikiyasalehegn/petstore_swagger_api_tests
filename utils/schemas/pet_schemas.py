GET_PET_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "status": {"type": "string"},
    },
    "required": ["id", "name", "status"]
}

ERROR_MESSAGE = {
  "type": "object",
  "properties": {
      "code": "integer",
      "type": "string",
      "message": "string"
  },
  "required": ["code", "message"]
}

CREATE_PET_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "category": {"type": "object"},
        "name": {"type": "string"},
        "photoUrls": {"type": "array", "items": {"type": "string"}},
        "tags": {"type": "array", "items": {"type": "object"}},
        "status": {"type": "string"},
    },
    "required": ["id", "name", "photoUrls", "status"]
}


GET_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "email": {"type": "string"},
        "password": {"type": "string"},
        "phone": {"type": "string"},
        "userstatus": {"type": "integer"},
    },
    "required": ["id", "username", "first_name", "last_name", "email", "phone", "userStatus"]
}











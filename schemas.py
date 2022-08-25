class UserSchema:
    registration = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "uuid": {"type": "integer"},
        },
        "required": ["message", "uuid"]
    }

    authentication = {
        "type": "object",
        "properties": {
            "access_token": {"type": "string"},
        },
        "required": ["access_token"]
    }

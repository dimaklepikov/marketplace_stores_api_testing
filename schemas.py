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
    

class StoreSchema:
    create_and_get = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "uuid": {"type": "integer"},
            "items": {"type": "array"},
        },
        "required": ["name", "uuid", "items"]
    }
    
    existing_store_cretion = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
        },
        "required": ["message"]    
    }


class ItemSchema:
    create_and_get = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "price": {"type": "integer"},
            "itemID": {"type": "integer"},
            "description": {"type": "string"},
            "image": {"type": "string"},
        },
        "required": ["name", "price", "itemID", "description", "image"]         
    }

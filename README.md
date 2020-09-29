# real-estate-app
## Ewan Watson
## 28/09/2020

## Database Schema
```json
{
    "Listing": {
        "id": {
            "type": "int",
        },
        "realtor": {
            "type": "int",
            "foreign_key": "realtor"
        },
        "title": {
            "type": "string"
        },
        "description": {
            "type": "text"
        },
        "price": {
            "type": "int"
        },
        "bedrooms": {
            "type": "int"
        },
        "bathrooms": {
            "type": "float"
        },
        "garages": {
            "type": "int",
            "default": 0
        },
        "sqft": {
            "type": "int"
        },
        "land": {
            "type": "float"
        },
        "photo_main": {
            "type": "string"
        },
        "photo_1": {
            "type": "string"
        },
        "photo_2": {
            "type": "string"
        },
        "photo_3": {
            "type": "string"
        },
        "photo_4": {
            "type": "string"
        },
        "photo_5": {
            "type": "string"
        },
        "photo_6": {
            "type": "string"
        },
        "list_date": {
            "type": "date"
        },
        "address": {
            "type": "string"
        },
        "city": {
            "type": "string"
        },
        "county": {
            "type": "string"
        },
        "postcode": {
            "type": "string"
        },
        "is_published": {
            "type": "bool",
            "default": true
        },
    },
    "Realtor": {
        "id": {
            "type": "int"
        },
        "name": {
            "type": "string"
        },
        "photo": {
            "type": "string"
        },
        "description": {
            "type": "text"
        },
        "email": {
            "type": "string"
        },
        "phone": {
            "type": "string"
        },
        "is_mvp": {
            "type": "bool",
            "default": false
        },
        "hire_date": {
            "type": "date"
        }
    },
    "Contact": {
        "id": {
            "type": "int"
        },
        "user_id": {
            "type": "int"
        },
        "listing": {
            "type": "string"
        },
        "listing_id": {
            "type": "int"
        },
        "name": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "phone": {
            "type": "string"
        },
        "message": {
            "type": "text"
        },
        "contact_date": {
            "type": "date"
        }
    }
}
```
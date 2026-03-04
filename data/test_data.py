from utils.utility_functions import random_string
import datetime


class PetsData:
    INVALID_ID = 'invalid id'
    INVALID_API_KEY = 'invalid api key'
    INVALID_PET_STATUS = 'invalid pet status'
    AVAILABLE_PETS = "available"
    PENDING_PETS = "pending"
    SOLD_PETS = "sold"
    VALID_ID = None
    PET_NAME = 'Richey'
    PET_PIC = 'https://www.four-paws.org/our-stories/publications-guides/10-tips-to-recognise-a-responsible-puppy-seller'
    CREATE_PET_WITH_VALID_DATA = {
      "id": 0,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }
    CREATE_PET_WITH_EMPTY_DATA = {}
    CREATE_PET_WITH_INVALID_ID = {
      "id": "345tdfsdvdsf",
      "name": "Mkkk",
      "photoUrls": [],
      "tags": [],
      "status": "available"
    }
    CREATE_PET_WITH_INVALID_STATUS = {
      "name": "Status",
      "photoUrls": [],
      "tags": [],
      "status": INVALID_PET_STATUS
    }
    CREATE_PET_WITHOUT_NAME = {
      "category": {},
      "photoUrls": [],
      "tags": [],
      "status": INVALID_PET_STATUS
    }

    Update_PET_WITH_VALID_DATA= {
      "id": None,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": random_string(8),
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

    Update_PET_WITH_INVALID_DATA = {
        "id": "asdfv,",
        "category": {
            "id": "hsdvck-=21340",
            "name": 65756
        },
        "name": "jscvjm",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": 2345476
    }

    UPDATE_PET_WITHOUT_ID = {
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": random_string(8),
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }



class OrderPetsData:
    INVALID_ID = "fhgjg"
    ORDER_PET_WITH_VALID_DATA = {
    "id": None,
    "petId": None,
    "quantity": 0,
    "shipDate": str(datetime.date.today()),
    "status": "placed",
    "complete": True
}

    ORDER_PET_WITH_INVALID_DATA = {
        "id": "7384RTKJHQCD",
        "petId": "AD87T134R",
        "quantity": True,
        "shipDate": False,
        "status": 2345,
        "complete": "weg6"
    }

class UsrData:
    CREATE_USERS_WITH_VALID_DATA = [
      {
        "username": "User01",
        "firstName": "User",
        "lastName": "One",
        "email": "user01@gmail.com",
        "password": "123456",
        "phone": "0489732567",
        "userStatus": 0
      },
      {
        "username": "User02",
        "firstName": "User2",
        "lastName": "Two",
        "email": "user02@gmai.com",
        "password": "7654321",
        "phone": "03789469235",
        "userStatus": 1
      }
    ]


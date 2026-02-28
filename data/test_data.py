class PetsData:
    INVALID_ID = 'invalid id'
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



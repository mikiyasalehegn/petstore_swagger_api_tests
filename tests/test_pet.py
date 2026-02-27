from utils.endpoints import PetEndpoints
from utils.assertion import assert_status_code, assert_data_schema, assert_key, assert_pet_statuses, assert_error_messages
from utils.schemas import pet_schemas
from data.test_data import PetsData


def test_create_pet_with_valid_data(pet_api):
    response = pet_api.create_pet(PetsData.CREATE_PET_WITH_VALID_DATA)
    assert_status_code(response, 201)
    assert_data_schema(response, pet_schemas.create_pet_schema)

def test_create_pet_with_empty_data(pet_api):
    response = pet_api.create_pet(PetsData.CREATE_PET_WITH_EMPTY_DATA)
    assert_status_code(response, 400)
    assert_error_messages(response, "Id should be integer")

def test_create_pet_with_invalid_api_key(pet_api):
    invalid_api_key = "wrong key"
    response = pet_api.create_pet(PetsData.CREATE_PET_WITH_VALID_DATA, headers=invalid_api_key)
    assert_status_code(response, 404)

def test_create_pet_with_invalid_id(pet_api):
    response = pet_api.create_pet(PetsData.CREATE_PET_WITH_INVALID_ID)
    assert_status_code(response, 400)


def test_get_pet_by_correct_id(pet_api):
    response = pet_api.get_pet(10)
    assert_status_code(response, 200)
    assert_data_schema(response, pet_schemas.get_pet_schema)

def test_get_pet_by_invalid_id(pet_api):
    response = pet_api.get_pet(PetsData.VALID_ID)
    assert_status_code(response, 404)

def test_get_available_pets(pet_api):
    response = pet_api.get_pet(PetEndpoints.FIND_BY_STATUS("available"))
    assert_status_code(response, 200)
    assert_pet_statuses(response, PetsData.AVAILABLE_PETS)

def test_get_pending_pets(pet_api):
    response = pet_api.get_pet(PetEndpoints.FIND_BY_STATUS("pending"))
    assert_status_code(response, 200)
    assert_pet_statuses(response, PetsData.PENDING_PETS)

def test_get_sold_pets(pet_api):
    response = pet_api.get_pet(PetEndpoints.FIND_BY_STATUS("sold"))
    assert_status_code(response, 200)
    assert_pet_statuses(response, PetsData.SOLD_PETS)

def test_get_pets_with_invalid_status(pet_api):
    response = pet_api.get_pet(PetEndpoints.FIND_BY_STATUS(PetsData.INVALID_PET_STATUS))
    assert_status_code(response, 404)
    assert_data_schema(response, pet_schemas.error_message)
    assert_error_messages(response, "Invalid pet status")






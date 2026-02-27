from conftest import api_client
from utils.endpoints import PetEndpoints
from utils.assertion import assert_status_code, assert_data_schema, assert_key, assert_pet_statuses, assert_error_messages
from utils.schemas import pet_schemas
from data.test_data import PetsData




def test_get_pet_by_correct_id(api_client):
    pet_id = 100
    response = api_client.get(PetEndpoints.GET_BY_ID.format(pet_id))
    assert_status_code(response, 200)
    assert_data_schema(response, pet_schemas.get_pet_schema)

def test_get_pet_by_invalid_id(api_client):
    response = api_client.get(PetEndpoints.GET_BY_ID.format(PetsData.VALID_ID))
    assert_status_code(response, 404)

def test_get_available_pets(api_client):
    response = api_client.get(PetEndpoints.FIND_BY_STATUS.format(PetsData.AVAILABLE_PETS))
    assert_status_code(response, 200)
    assert_pet_statuses(response, PetsData.AVAILABLE_PETS)

def test_get_pending_pets(api_client):
    response = api_client.get(PetEndpoints.FIND_BY_STATUS.format(PetsData.PENDING_PETS))
    assert_status_code(response, 200)
    assert_pet_statuses(response, PetsData.PENDING_PETS)

def test_get_sold_pets(api_client):
    response = api_client.get(PetEndpoints.FIND_BY_STATUS.format(PetsData.SOLD_PETS))
    assert_status_code(response, 200)
    assert_pet_statuses(response, PetsData.SOLD_PETS)

def test_get_pets_with_invalid_status(api_client):
    response = api_client.get(PetEndpoints.FIND_BY_STATUS.format(PetsData.INVALID_PET_STATUS))
    assert_status_code(response, 404)
    assert_data_schema(response, pet_schemas.error_message)
    assert_error_messages(response, "Invalid pet status")






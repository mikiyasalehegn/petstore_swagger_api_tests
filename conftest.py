import pytest
from api.order_api import OrderApi
from utils.api_client import APIClient
from api.pet_api import PetApi


@pytest.fixture(scope="session")
def api_client():
    return APIClient()

@pytest.fixture(scope="session")
def order_api(api_client):
    return OrderApi(api_client)

@pytest.fixture(scope="session")
def pet_api(api_client):
    return PetApi(api_client)

# @pytest.fixture(scope="session")
# def created_pet(pet_api):
#     response = pet_api.create_pet(PetsData.CREATE_PET_WITH_VALID_DATA)
#
#     pet_id = response.json().get("id")
#
#     return pet_id
#
#     # clean the id after all test run
#     # pet_api.delete_pet(pet_id)
from utils.endpoints import PetEndpoints
from utils.assertion import assert_status_code


def test_get_pet(api_client):
    pet_id = 100
    response = api_client.get(PetEndpoints.GET_BY_ID.format(pet_id))
    print(response.json())
    assert_status_code(response, 200)

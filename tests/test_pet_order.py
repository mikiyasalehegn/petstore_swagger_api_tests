from utils.assertion import assert_data_schema, assert_status_code, assert_error_messages
from utils.schemas import order_schemas
from data.test_data import OrderPetsData
from utils.utility_functions import update_keys

def test_get_store_inventory(order_api):
    response = order_api.get_store_inventory()
    assert_status_code(response, 200)
    assert_data_schema(response, order_schemas.get_store_inventory_schema)

def test_get_store_inventory_with_invalid_api_key(order_api):
    response = order_api.get_store_inventory(api_key="invalid_api_key")
    assert_status_code(response, 404)
    assert_error_messages(response, "invalid_api_key")

def test_place_pet_order_with_valid_data(order_api):
    payload = update_keys(OrderPetsData.ORDER_PET_WITH_VALID_DATA, petId=1, id=2)
    response = order_api.place_pet_order(payload=payload)
    assert_status_code(response, 201)

def test_duplicate_order(order_api):
    # The api should detect the duplication since the order is already exist
    payload = update_keys(OrderPetsData.ORDER_PET_WITH_VALID_DATA, petId=1, id=2)
    response = order_api.place_pet_order(payload)
    assert_status_code(response, 409)

def test_place_pet_order_with_invalid_data(order_api):
    response = order_api.place_pet_order(payload=OrderPetsData.ORDER_PET_WITH_INVALID_DATA)
    assert_status_code(response, 400)

def test_place_pet_order_with_invalid_api_key(order_api):
    payload = update_keys(OrderPetsData.ORDER_PET_WITH_VALID_DATA, petId=1, id=2)
    response = order_api.place_pet_order(payload, api_key="invalid_api_key")
    assert_status_code(response, 404)
    assert_error_messages(response, "invalid_api_key")

def test_place_pet_order_with_empty_payload(order_api):
    response = order_api.place_pet_order({})
    assert_status_code(response, 400)

def test_get_order(order_api):
    payload = update_keys(OrderPetsData.ORDER_PET_WITH_VALID_DATA, petId=1, id=2)
    create_order_response = order_api.place_pet_order(payload)
    assert_status_code(create_order_response, 200)
    order_id = create_order_response.json()["id"]
    response = order_api.get_pet_order(order_id)
    assert_status_code(response, 200)
    assert response.json().get("id") == order_id
    assert_data_schema(response, order_schemas.PLACE_ORDER_PET_SCHEMA)

def test_get_order_with_invalid_api_key(order_api):
    payload = update_keys(OrderPetsData.ORDER_PET_WITH_VALID_DATA, petId=1, id=2)
    create_order_response = order_api.place_pet_order(payload)
    assert_status_code(create_order_response, 200)
    order_id = create_order_response.json()["id"]
    response = order_api.get_pet_order(order_id, api_key="invalid_api_key")
    assert_status_code(response, 404)

def test_get_order_with_invalid_order_id(order_api):
    response = order_api.get_pet_order("384768rbnsdc")
    assert_status_code(response, 404)
    assert_error_messages(response, "invalid order id")

def test_delete_order(order_api):
    payload = update_keys(OrderPetsData.ORDER_PET_WITH_VALID_DATA, petId=1, id=2)
    create_order_response = order_api.place_pet_order(payload)
    assert_status_code(create_order_response, 200)
    order_id = create_order_response.json()["id"]
    response = order_api.delete_pet_order(order_id)
    assert_status_code(response, 200)

def test_delete_order_with_invalid_order_id(order_api):
    response = order_api.delete_pet_order("384768rbnsdc")
    assert_status_code(response, 404)
    assert_error_messages(response, "invalid order id")

def test_delete_order_with_invalid_api_key(order_api):
    response = order_api.delete_pet_order(order_id=2, api_key="invalid_api_key")
    assert_status_code(response, 404)
    assert_error_messages(response, "invalid api key")
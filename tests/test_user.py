from utils.schemas.user_schema import GET_USER_SCHEMA
from utils.assertion import assert_data_schema, assert_status_code, assert_error_messages
from data.test_data import UsrData

def test_create_test_with_list_and_valid_data(user_api):
    response = user_api.create_multiple_users(payload=UsrData.CREATE_USERS_WITH_VALID_DATA)
    assert_status_code(response, 200)








from utils.schemas.user_schema import GET_USER_SCHEMA
from utils.assertion import assert_data_schema, assert_status_code, assert_error_messages
from data.test_data import UsrData
from utils.utility_functions import update_keys


def test_create_users_with_list_and_valid_data(user_api):
    response = user_api.create_multiple_users(payload=UsrData.CREATE_USERS_WITH_VALID_DATA)
    assert_status_code(response, 200)

def test_create_users_with_existing_users_data(user_api):
    response = user_api.create_multiple_users(payload=UsrData.CREATE_USERS_WITH_VALID_DATA)
    assert_status_code(response, 409)

def test_create_users_with_duplicated_users_data(user_api):
    response = user_api.create_multiple_users(UsrData.CREATE_USERS_WITH_DUPLICATED_VALID_DATA)
    assert_status_code(response, 409)

def test_create_users_with_invalid_email(user_api):
    payload = update_keys(data=UsrData.CREATE_USERS_WITH_VALID_DATA[0], email="skdcbk")
    response = user_api.create_multiple_users(payload=payload)
    assert_status_code(response, 400)

def test_create_users_with_invalid_data(user_api):
    response = user_api.create_multiple_users(payload=UsrData.CREATE_USERS_WITH_INVALID_DATA)
    assert_status_code(response, 400)
    assert_error_messages(response, "Invalid data is provided")

def test_create_users_with_invalid_api_key(user_api):
    response = user_api.create_multiple_users(payload=UsrData.CREATE_USERS_WITH_VALID_DATA, api_key="invalid api key")
    assert_status_code(response, 404)
    assert_error_messages(response, "Invalid api key")

def test_create_user_with_valid_data(user_api):
    response = user_api.create_user(payload=UsrData.CREATE_USER_WITH_VALID_DATA)
    assert_status_code(response, 200)

def test_get_user_name(user_api):
    response = user_api.get_user(user_name=UsrData.CREATE_USER_WITH_VALID_DATA["username"])
    assert_status_code(response, 200)
    assert_data_schema(response, GET_USER_SCHEMA)

def test_get_user_by_invalid_api_key(user_api):
    response = user_api.get_user(user_name=UsrData.CREATE_USERS_WITH_VALID_DATA["username"], api_key="invalid api key")
    assert_status_code(response, 404)

def test_get_user_by_non_existing_user_name(user_api):
    response = user_api.get_user(user_name=UsrData.RANDOM_USER_NAME)
    assert_status_code(response, 404)

def test_update_user_with_valid_data(user_api):
    username = UsrData.CREATE_USER_WITH_VALID_DATA["username"]
    update_user_data = update_keys(data=UsrData.CREATE_USER_WITH_VALID_DATA, username=UsrData.RANDOM_USER_NAME,
                                   firstName=UsrData.RANDOM_FIRST_NAME, lastName=UsrData.RANDOM_LAST_NAME,
                                   email=UsrData.RANDOM_USER_EMAIL, password=UsrData.RANDOM_USER_PASSWORD,
                                   userStatus=3)
    response = user_api.update_user(user_name=username, payload=update_user_data)
    assert_status_code(response, 200)
    new_username = response.json()["username"]
    get_user_response = user_api.get_user(user_name=new_username)
    assert_status_code(get_user_response, 200)
    assert_data_schema(get_user_response, GET_USER_SCHEMA)
    if response.status_code == 200:
        UsrData.CREATE_USER_WITH_VALID_DATA["username"] = new_username
        UsrData.CREATE_USER_WITH_VALID_DATA["password"] = response.json()["password"]
    UsrData.CREATE_USER_WITH_VALID_DATA["password"] = response.json()["password"]
    assert get_user_response.json()["username"] == update_user_data["username"]
    assert get_user_response.json()["firstName"] == update_user_data["firstName"]
    assert get_user_response.json()["lastName"] == update_user_data["lastName"]
    assert get_user_response.json()["email"] == update_user_data["email"]
    assert get_user_response.json()["password"] == update_user_data["password"]
    assert get_user_response.json()["userStatus"] == update_user_data["userStatus"]

def test_update_user_invalid_data(user_api):
    username = UsrData.CREATE_USER_WITH_VALID_DATA["username"]
    response = user_api.update_user(user_name=username, payload=UsrData.CREATE_USER_WITH_INVALID_DATA)
    if response.status_code == 200:
        UsrData.CREATE_USER_WITH_VALID_DATA["username"] = response.json()["username"]
    assert_status_code(response, 400)

def test_update_user_id(user_api):
    username = UsrData.CREATE_USERS_WITH_VALID_DATA[0]["username"]
    response = user_api.update_user(user_name=username, payload={"id": 123})
    assert_status_code(response, 400)

def test_update_non_existing_user(user_api):
    username = UsrData.RANDOM_USER_NAME
    response = user_api.update_user(user_name=username, payload=UsrData.CREATE_USER_WITH_VALID_DATA)
    assert_status_code(response, 404)

def test_update_user_with_invalid_email(user_api):
    email = UsrData.INVALID_USER_EMAIL
    username = UsrData.CREATE_USER_WITH_VALID_DATA["username"]
    response = user_api.update_user(user_name=username, payload={"email": email})
    assert_status_code(response, 400)

def test_login_user(user_api):
    username = UsrData.CREATE_USER_WITH_VALID_DATA["username"]
    password = UsrData.CREATE_USER_WITH_VALID_DATA["password"]
    response = user_api.login(username=username, password=password)
    assert_status_code(response, 200)

def test_login_user_with_wrong_password(user_api):
    username = UsrData.CREATE_USER_WITH_VALID_DATA["username"]
    password = UsrData.CREATE_USER_WITH_INVALID_DATA["password"]
    response = user_api.login(username=username, password=password)
    assert_status_code(response, 401)
    assert_error_messages(response, "Wrong password")

def test_login_user_with_invalid_username(user_api):
    username = UsrData.RANDOM_USER_NAME
    password = UsrData.CREATE_USER_WITH_VALID_DATA["password"]
    response = user_api.login(username=username, password=password)
    assert_status_code(response, 401)
    assert_error_messages(response, "User does not exist")

def test_login_user_with_invalid_password_and_username(user_api):
    username = UsrData.RANDOM_USER_NAME
    password = UsrData.RANDOM_USER_PASSWORD
    response = user_api.login(username=username, password=password)
    assert_status_code(response, 400)
    assert_error_messages(response, "Wrong password and username")

def test_login_with_invalid_api_key(user_api):
    username = UsrData.CREATE_USER_WITH_VALID_DATA["username"]
    response = user_api.login(username=username, api_key="invalid api key")
    assert_status_code(response, 401)
    assert_error_messages(response, "Invalid api key")

def test_delete_user(user_api):
    username = UsrData.CREATE_USER_WITH_VALID_DATA["username"]
    response = user_api.delete_user(user_name=username)
    assert_status_code(response, 200)
    response = user_api.get_user(user_name=username)
    assert_status_code(response, 404)

def test_delete_non_existing_user(user_api):
    username = UsrData.RANDOM_USER_NAME
    response = user_api.delete_user(user_name=username)
    assert_status_code(response, 404)
    assert_error_messages(response, "User does not exist")

def test_delete_user_with_invalid_api_key(user_api):
    username = UsrData.CREATE_USERS_WITH_VALID_DATA[1]
    response = user_api.delete_user(user_name=username)
    assert_status_code(response, 401)
    assert_error_messages(response, "Invalid api key")

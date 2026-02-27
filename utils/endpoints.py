class PetEndpoints:
    CREATE = "/pet"
    UPDATE = "/pet"
    GET_BY_ID = "/pet/{}"
    DELETE = "/pet/{}"
    FIND_BY_STATUS = lambda entity: f"findByStatus?status={entity}"


class UserEndpoints:
    LOGIN = "/user/login"
    LOGOUT = "/user/logout"
    CREATEWITHLIST = "/user/createWithList"
    GET_USER = "user/{}"
    UPDATE_USER_NAME = "user/{}"
    DELETE_USER = "/user/{}"
    CREATE_USERS = "/user/createWithArray"
    CREATE_USER = "/user"


class PetStore:
    GET_STORE_INVENTORY = "store/inventory"
    ORDER_PET = "/store/order"
    GET_ORDER_BY_ID = "/store/order"
    DELETE_ORDER_BY_ID = "/store/order/{}"
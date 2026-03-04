class UserApi:
    def __init__(self, api_client):
        self.api_client = api_client

    def create_multiple_users(self, payload, api_key=None):
        return self.api_client.post("/user/createWithList", json=payload, api_key=api_key)

    def create_user(self, payload, api_key=None):
        return self.api_client.post("/user", json=payload, api_key=api_key)

    def get_user(self, user_name, api_key=None):
        return self.api_client.get(f"/user/{user_name}", api_key=api_key)

    def update_user(self, user_name, api_key=None):
        return self.api_client.put(f"/user/{user_name}", api_key=api_key)

    def delete_user(self, user_name, api_key=None):
        return self.api_client.delete(f"/user/{user_name}", api_key=api_key)

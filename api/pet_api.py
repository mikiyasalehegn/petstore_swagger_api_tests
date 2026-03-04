class PetApi:
    def __init__(self, api_client):
        self.api_client = api_client

    def create_pet(self, payload, api_key=None):
        return self.api_client.post("/pet", api_key=api_key, json=payload)

    def get_pet(self, entity, api_key=None):
        return self.api_client.get(f"/pet/{entity}", api_key=api_key)

    def delete_pet(self, entity, api_key=None):
        return self.api_client.delete(f"/pet/{entity}", api_key=api_key)

    def update_pet(self, payload, api_key=None):
        return self.api_client.put("/pet", json=payload, api_key=api_key)

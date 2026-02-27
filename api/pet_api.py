class PetApi:
    def __init__(self, api_client):
        self.api_client = api_client

    def create_pet(self, payload):
        return self.api_client.post("/pet", json=payload)

    def get_pet(self, entity):
        return self.api_client.get(f"/pet/{entity}")

    def delete_pet(self, entity):
        return self.api_client.delete(f"/pet/{entity}")

    def update_pet(self, pet_id, payload):
        return self.api_client.put(f"/pet/{pet_id}", json=payload)
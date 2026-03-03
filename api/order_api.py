class OrderApi:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_store_inventory(self, api_key=None):
        return self.api_client.get(f"/store/inventory", api_key=api_key)

    def get_pet_order(self, order_id, api_key=None):
        return self.api_client.get(f"/store/order/{order_id}", api_key=api_key)

    def place_pet_order(self, payload, api_key=None):
        return self.api_client.post("/store/order", json=payload, api_key=api_key)

    def delete_pet_order(self, order_id, api_key=None):
        return self.api_client.delete(f"/store/order/{order_id}", api_key=api_key)
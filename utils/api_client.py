import requests
from utils.config import BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()

    def get(self, endpoint, **kwargs):
        return self.session.get(self.base_url + endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.session.post(self.base_url + endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.session.put(self.base_url + endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self.session.patch(self.base_url + endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.session.delete(self.base_url + endpoint, **kwargs)


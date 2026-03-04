import requests
from utils.config import BASE_URL,API_KEY

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()

    @staticmethod
    def _prepare_headers(api_key, headers):
        final_headers = dict(headers).copy() if headers else {}
        final_headers["api-key"] = api_key if api_key else API_KEY
        return final_headers

    def get(self, endpoint, api_key=None, **kwargs):
        headers = self._prepare_headers(api_key, kwargs.pop("headers", None))
        return self.session.get(self.base_url + endpoint, headers=headers, **kwargs)

    def post(self, endpoint, api_key=None, **kwargs):
        headers = self._prepare_headers(api_key, kwargs.pop("headers", None))
        return self.session.post(self.base_url + endpoint, headers=headers, **kwargs)

    def put(self, endpoint, api_key=None, **kwargs):
        headers = self._prepare_headers(api_key, kwargs.pop("headers", None))
        return self.session.put(self.base_url + endpoint, headers=headers, **kwargs)

    def patch(self, endpoint, api_key=None, **kwargs):
        headers = self._prepare_headers(api_key, kwargs.pop("headers", None))
        return self.session.patch(self.base_url + endpoint,headers=headers, **kwargs)

    def delete(self, endpoint, api_key=None, **kwargs):
        headers = self._prepare_headers(api_key, kwargs.pop("headers", None))
        return self.session.delete(self.base_url + endpoint,headers=headers, **kwargs)

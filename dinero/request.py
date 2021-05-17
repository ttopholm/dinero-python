import requests
from .exceptions import *


def with_error_handling(callback, *args, **kwargs):

    response = callback(*args, **kwargs)
    # response.raise_for_status()
    r = response.json()

    if "validationErrors" in r:
        raise RequestError(r["validationErrors"])
    elif "errors" in r:
        raise RequestError(", ".join(r["errors"]))
    elif "Collection" in r:
        result = r["Collection"]
    elif "message" in r:
        result = r["message"]
    else:
        result = r
    return result


class Request:
    def __init__(self, version="v1"):
        self.base = "https://api.dinero.dk/"
        self.version = None
        self.access_token = None
        self.headers = {}
        self.set_version(version)
        self.organization_id = None

    def set_version(self, version):
        self.version = f"{version}/"

    def set_organization_id(self, organization_id):
        self.organization_id = f"{organization_id}/"

    def set_auth_header(self, token):
        self.headers["Authorization"] = (
            token["token_type"] + " " + token["access_token"]
        )

    def make_url(self, trailing_uri):
        return self.base + self.version + str(self.organization_id) + trailing_uri

    def get(self, endpoint, payload=None):
        return with_error_handling(
            requests.get, self.make_url(endpoint), headers=self.headers, params=payload
        )

    def post(self, endpoint, payload=None):
        return with_error_handling(
            requests.post, self.make_url(endpoint), headers=self.headers, json=payload
        )

    def put(self, endpoint, payload=None):
        return with_error_handling(
            requests.put, self.make_url(endpoint), headers=self.headers, json=payload
        )

    def delete(self, endpoint):
        return with_error_handling(
            requests.delete, self.make_url(endpoint), headers=self.headers
        )

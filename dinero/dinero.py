import requests
from .request import Request
from .endpoints import Endpoint, BookEndpoint, PaymentEndpoint


def create_endpoint_object(name, inherits_from):
    return type(name, (inherits_from, object), {})


class Dinero:
    endpoints = {"Invoice": "invoices", "Contact": "contacts"}

    custom_endpoints = {
        "Book": (BookEndpoint, "invoices"),
        "Payment": (PaymentEndpoint, "invoices"),
    }

    def __init__(self, client_id: str, client_secret: str):
        self.request = Request()
        self.dinero_auth_endpoint = "https://authz.dinero.dk/dineroapi/oauth/token"
        self.client_id = client_id
        self.client_secret = client_secret

    def __getattr__(self, name):
        obj_name = name.capitalize()

        if obj_name in self.endpoints:
            e = create_endpoint_object(obj_name, Endpoint)
            endpoint = e(self.request, self.endpoints[obj_name])
        elif obj_name in self.custom_endpoints:
            obj_base, endpoint_name = self.custom_endpoints[obj_name]
            e = create_endpoint_object(obj_name, obj_base)
            endpoint = e(self.request, endpoint_name)
        else:
            raise RuntimeError("No such API object: " + name)

        return endpoint

    def authenticate(self, organization_api_key: str, organization_id: int):
        data = {
            "grant_type": "password",
            "scope": "read write",
            "username": organization_api_key,
            "password": organization_api_key,
        }
        r = requests.post(
            self.dinero_auth_endpoint,
            data=data,
            auth=(self.client_id, self.client_secret),
        )
        if r.status_code == 200:
            self.request.set_auth_header(r.json())
            self.request.set_organization_id(organization_id)

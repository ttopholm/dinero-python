from functools import reduce
from .exceptions import *
#from .dto.product import Product
from importlib import import_module

class BaseEndpoint(object):

    def __init__(self, request, endpoint):
        self.request = request
        self.endpoint = endpoint
        cls_name = self.__class__.__name__
        module = import_module(f'dinero.dto.{cls_name.lower()}')
        self.cls = getattr(module, cls_name.capitalize())

    def _url_with(self, *params):
        def add_to_endpoint(endpoint, param):
            return endpoint + "/" + str(param)

        return reduce(add_to_endpoint, params, self.endpoint)


class Endpoint(BaseEndpoint):

    def get(self, id):
        return self.cls.from_dict(self.request.get(self._url_with(id)))

    def update(self, id, params):
        if type(params) in [self.cls]:
            params = params.to_dict()
        return self.request.put(self._url_with(id), payload=params)

    def remove(self, id):
        return self.request.delete(self._url_with(id))

    def list(self):
        results = self.request.get(self.endpoint)
        lst = []
        for result in results:
            p = self.get(result.get(self.cls.get_id_field()))
            lst.append(p)
        return lst

    def find_by(self, params):
        try:
            results = self.request.get(self.endpoint, payload=params)
            lst = []
            for result in results:
                p = self.get(result.get(self.cls.get_id_field()))
                lst.append(p)
            return lst
        except RequestError:  # If we can't find the resource
            return None

    def create(self, params):
        if type(params) == self.cls:
            params = params.to_dict()

        return self.request.post(self.endpoint, payload=params)


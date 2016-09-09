from alexandria.client.alexandria import *
from alexandria.client.resource_prototype import ResourcePrototype

from alexandria.notebook.resource_proxy import ResourceProxy


class AlexandriaProxy:
    def __init__(self, server_url, admin_key="admin"):
        self.alexandria = Alexandria(server_url, admin_key=admin_key)

    def __dir__(self):
        return ['create_resource', 'get_resource']

    def create_resource(self, resource_id):
        uuid = self.alexandria.resources.add(ResourcePrototype(resource_id)).uuid
        rp = ResourceProxy(resource_id, uuid, self.alexandria)
        return rp

    def get_resource(self, resource_id):
        uuid = ''
        rp = ResourceProxy(resource_id, uuid, self.alexandria)
        return rp

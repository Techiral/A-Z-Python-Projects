from flask_injector import inject
from providers.CouchProvider import CouchProvider


@inject(data_provider=CouchProvider)
def read_product(data_provider) -> str:
    return data_provider.read_product()
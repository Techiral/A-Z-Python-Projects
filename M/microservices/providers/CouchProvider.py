import requests
product = {
        "_id":"123",
        "prodname": "First product",
        "catagory": "catagory1",
        "quantity": "4"
        }

class CouchProvider(object):
    
    def read_product(self) -> str:
        return product,200
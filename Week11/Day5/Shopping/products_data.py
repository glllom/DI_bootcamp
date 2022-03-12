import json


def retrieve_all_products(file_path='data/products.json'):
    with open(file_path, 'r') as f:
        all_products = json.load(f)
    return all_products


def retrieve_requested_product(id, file_path='data/products.json'):
    for product in retrieve_all_products(file_path):
        if product["ProductId"] == id:
            return product



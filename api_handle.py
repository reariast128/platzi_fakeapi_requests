import requests

def get_categories():
    API_URL = "https://api.escuelajs.co/api/v1/categories"
    response = requests.get(API_URL)
    return response
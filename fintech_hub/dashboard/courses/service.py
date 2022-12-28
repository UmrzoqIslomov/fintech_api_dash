import requests


def get_courses():
    url = 'http://127.0.0.1:8000/api/v1/courses/'
    response = requests.get(url)
    return response.json()

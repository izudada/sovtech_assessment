import requests
from ariadne import convert_kwargs_to_snake_case


def resolve_persons(obj, info, page):
    try:
        url = f"https://swapi.dev/api/people/?page={page}"

        response = requests.get(url)
        result = response.json()["results"]

        persons = [person for person in result]
        payload = {
            "success": True,
            "persons": persons
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

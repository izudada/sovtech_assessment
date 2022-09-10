from time import perf_counter
import requests
from ariadne import convert_kwargs_to_snake_case


def make_api_call(page):
    try:
        url = f"https://swapi.dev/api/people/?page={page}"
    except Exception as error:
        print(error)
        return False

    response = requests.get(url)
    result = response.json()["results"]
    return result


def resolve_persons(obj, info, page):
    try:
        result = make_api_call(page)

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

@convert_kwargs_to_snake_case
def resolve_person(obj, info, person_name):
    try:
        url = f"https://swapi.dev/api/people//?search={person_name}"

        response = requests.get(url)
        person = response.json()["results"]
        payload = {
            "success": True,
            "person": person[0]
        }

    except AttributeError:  # person not found
        payload = {
            "success": False,
            "errors": [f"Person matching name  not found"]
        }

    return payload

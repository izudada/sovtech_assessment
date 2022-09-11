import requests
from ariadne import convert_kwargs_to_snake_case


base_url = "https://swapi.dev/api/people/"

def resolve_persons(obj, info, page):
    """
        A REST API wrapper/resolver that returns list of
        persons or people.
        Parameters : obj (a value returned by a parent resolver) 
                    info (contains any context information that the GraphQL server provided)
                    page (pagination for the REST API) 

        Returns : payload (of persons if successful and error if else)

    """
    try:
        url = base_url + f"?page={page}"
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

@convert_kwargs_to_snake_case
def resolve_person(obj, info, person_name):
    try:
        url = base_url + f"?search={person_name}"

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

from urllib import request
import requests
from ariadne import convert_kwargs_to_snake_case
from flask import jsonify, request as rq
import jwt
from api import app, Users


base_url = "https://swapi.dev/api/people/"


def token_required():
    if 'Authorization' in rq.headers:
        main_token = rq.headers["Authorization"].split(' ')
        jwt_token = main_token[1]

    if not jwt_token:
        return False
    try:
        data = jwt.decode(jwt_token, app.config['SECRET_KEY'], algorithms=["HS256"])
        current_user = Users.query.filter_by(public_id=data['public_id']).first()
    except Exception as error:
        print(error)
        return False

    return current_user
    

def resolve_persons(obj, info, page):
    """
        A REST API wrapper/resolver that returns list of
        persons or people.
        Parameters : obj (a value returned by a parent resolver) 
                    info (contains any context information that the GraphQL server provided)
                    page (pagination for the REST API) 

        Returns : payload (of persons if successful and error if else)

    """
    auth = token_required()
    if not auth:
        payload = {
            "success": False,
            "errors": [str(auth)]
        }

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
    """
        A REST API wrapper/resolver that returns a person object .
        Parameters : obj (a value returned by a parent resolver) 
                    info (contains any context information that the GraphQL server provided)
                    person_name (name value for REST API query) 

        Returns : payload (of a person object if successful and error if else)
    """
    print("Anthony")
    auth = token_required()
    if not auth:
        payload = {
        "success": False,
        "errors": [str(auth)]
    }
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
            "errors": [f"Person matching name {person_name} not found"]
        }

    return payload

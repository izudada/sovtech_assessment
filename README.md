# Backend Engineer Test By Sovtech

# Todos
- You should develop a GraphQL API
- Your GraphQL API should wrap the Star Wars API (https://swapi.dev/)
- It should have an authenticate Mutation that, when given an arbitrary username
    returns a JWT ( token ) with the username in the payload
- Your GraphQL API should have a Query type that resolves all People 
    (https://swapi.dev/api/people/), but only the Person's details (name, height, mass,
    gender, homeworld).
- The People Query should cater for pagination, you will notice the next property in
    the response. When given a page number, the respective People page should be
    returned (i.e. https://swapi.dev/api/people/?page=2)
- Your GraphQL API should have a Query type that resolves (searches for) a
    particular Person (People) given their name (i.e. https://swapi.dev/api/people/?
    search=Anakin Skywalker)
- All your Queries should check and validate a valid JWT issued from the
    authenticate Mutation ( token ) passed along, in the headers with each request.


### Install Dependencies

1. **Python 3.7** - You can install python with the follow instructions [here](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - Install a virtual environment uisng this resource [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

```bash
pip install -r requirements.txt
```


### Run the Server

You will need to create environmental variables by running:

```bash
    export FLASK_APP=main.py
    export FLASK_ENV=development
```
Then start server with:
```bash
    flask run
```

## API Documentation
This API has a database attached with existing dummy users whi has jwt tokens expiring in 5 days for easy testing. Thus import the postman collection "SovTech_GraphQL_Assessment.postman_collection.json" into postman.

### Getting started
- Base URL: The API is currently only accessible via your localhost server and can be accessed locally via http://127.0.0.1:5000/ or localhost:5000
- Authentication: No authentication or API keys are required to access the API at this time.


### Endpoints

-    Documentation for this endpoints can be found [here](https://documenter.getpostman.com/view/20677030/2s7YYoBRwB)


## Testing

To deploy the tests, run

Each postman endpoint has a test attached. You can also run tests as a colection.

### Useful resources

- [twilio blog](https://www.twilio.com/blog/graphql-api-python-flask-ariadne) - Build a GraphQL API with Python, Flask and Ariadne
- [bacancytechnology blog](https://www.bacancytechnology.com/blog/flask-jwt-authentication) - Flask JWT Authentication Tutorial

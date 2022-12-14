from api import app
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import resolve_persons, resolve_person
from api.mutation import resolve_create_user, resolve_login_user

#   Binding resolver to schema
query = ObjectType("Query")

query.set_field("persons", resolve_persons)
query.set_field("person", resolve_person)

mutation = ObjectType("Mutation")
mutation.set_field("createUser", resolve_create_user)
mutation.set_field("loginUser", resolve_login_user)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


#GraphQL endpoints

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug,
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

if  __name__ == '__main__': 
    app.run(debug=True)
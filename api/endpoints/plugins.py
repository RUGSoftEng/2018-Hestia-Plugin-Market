"""
Defines the plugins endpoint. A plugin represents a collection of files that can be added to a server.
"""
from flask_cors import (cross_origin)
from flask_restplus import (Resource, Namespace)
from api.authentication.authentication import (
    requires_auth
)
from api.database import session
from api.endpoints.expected_request_structures import PluginOptionsSchema

ns = Namespace(
    'plugins', description='List of all plugins available.')


@ns.route('/')
class PluginList(Resource):

    @ns.doc('list_plugins')
    @ns.expect(PluginOptionsSchema)
    @cross_origin(headers=["Access-Control-Allow-Origin", "*"])
    def get(self):
        # Gets a list of servers, depending on options specified by the plugin options schema.
        payload = ns.payload
        print(payload)
        posted_options_schema = PluginOptionsSchema().load(payload)
        options = posted_options_schema.load()
        s = session()

        return "Hello world"

    @ns.doc('create_plugin')
    @cross_origin(headers=["Content-Type", "Authorization"])
    @cross_origin(headers=["Access-Control-Allow-Origin", "*"])
    @requires_auth
    @ns.doc(security='apikey')
    def post(self):
        return "Goodbye"


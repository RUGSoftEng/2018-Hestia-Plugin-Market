"""
Defines the plugins endpoint. A plugin represents a collection of files that can be added to a server.
"""
from flask_cors import (cross_origin)
from flask_restplus import (Resource, Namespace, fields)
from api.authentication.authentication import (
    requires_auth
)
from api.database import session
from api.endpoints.expected_request_structures import PluginOptionsSchema

ns = Namespace(
    'plugins', description='List of all plugins available.')


POST_PLUGIN = ns.model('Plugin', {
    'name': fields.String(required=True),
    'version': fields.String(required=False),
    'description_short': fields.String(required=False),
    'description_long': fields.String(required=False),
    'tags': fields.List(fields.String(), required=False)
})


@ns.route('/')
class PluginList(Resource):

    @ns.doc('list_plugins')
    @cross_origin(headers=["Access-Control-Allow-Origin", "*"])
    def get(self):
        # Gets a list of servers, depending on options specified by the plugin options schema.
        posted_options_schema = PluginOptionsSchema().load(ns.payload)
        print(posted_options_schema)
        s = session()

        return "Hello world"

    @ns.doc('create_plugin')
    @ns.expect(POST_PLUGIN)
    @cross_origin(headers=["Content-Type", "Authorization"])
    @cross_origin(headers=["Access-Control-Allow-Origin", "*"])
    @requires_auth
    @ns.doc(security='apikey')
    def post(self):
        json = ns.payload
        print(json)
        return json


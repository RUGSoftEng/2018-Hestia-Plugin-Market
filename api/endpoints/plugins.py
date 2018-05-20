"""
Defines the plugins endpoint. A plugin represents a collection of files that can be added to a server.
"""
from flask import request
from flask_cors import (cross_origin)
from flask_restplus import (Resource, Namespace, fields)
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
    @cross_origin(headers=["Access-Control-Allow-Origin", "*"])
    def get(self):
        # Gets a list of servers, depending on options specified by the plugin options schema.
        #  Start by reading all optional arguments from the url params.
        count = request.args.get('count', default=10, type=int)
        page = request.args.get('page', default=1, type=int)
        author_id = request.args.get('author_id', default=None, type=str)
        title_contains = request.args.get('title_contains', default=None, type=str)
        sort_by = request.args.get('by', default='up_goats', type=str)
        sort_order = request.args.get('order', default='ASC', type=str)
        tags = request.args.getlist('tags', type=str)

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


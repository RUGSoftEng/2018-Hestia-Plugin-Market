"""
Defines the plugins endpoint. A plugin represents a collection of files that can be added to a server.
"""
from flask import (request)
from flask_cors import (cross_origin)
from flask_restplus import (
    Resource,
    Namespace,
    fields,
)
from api.authentication.authentication import (requires_auth)
from api.database import (SESSION)
from api.database.entities.plugin import (Plugin)

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

        return get_plugins_with_options(count,
                                        page,
                                        author_id,
                                        title_contains,
                                        sort_by,
                                        sort_order,
                                        tags)

    @ns.doc('create_plugin')
    @cross_origin(headers=["Content-Type", "Authorization"])
    @cross_origin(headers=["Access-Control-Allow-Origin", "*"])
    @requires_auth
    @ns.doc(security='apikey')
    def post(self):
        json = ns.payload
        print(json)
        return json


"""
Gets a list of plugins as a json string, given some parameters.
"""
def get_plugins_with_options(count, page, author_id, title_contains, sort_by, sort_order, tags):
    s = SESSION()
    q = s.query(Plugin.id,
                Plugin.name,
                Plugin.author_id,
                Plugin.version,
                Plugin.created_date,
                Plugin.last_edited_date,
                Plugin.description_short,
                Plugin.up_goats,
                Plugin.down_goats,
                Plugin.tags)\
        .limit(count)\
        .offset(count*(page-1))\
        .order_by(getattr(Plugin, sort_by) if sort_order == 'ASC' else getattr(Plugin, sort_by).desc())
    if author_id:
        q.filter_by(author_id = author_id)



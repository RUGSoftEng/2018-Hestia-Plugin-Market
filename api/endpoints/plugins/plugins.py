"""
Defines the plugins endpoint. A plugin represents a collection of files that can be added to a server.
"""
from flask import (jsonify)
from flask_cors import (cross_origin)
from flask_restplus import (Resource)
from api.authentication.authentication import (
    requires_auth,
    get_user_id,
)
from api.database.entities.entity import (
    SESSION,
    ENGINE,
    BASE,
)
from api.database.entities.model import (
    Plugin,
    PluginSchema
)
from api.endpoints.plugins import NAMESPACE

BASE.metadata.create_all(ENGINE)


@NAMESPACE.route('/')
class PluginList(Resource):
    '''Shows a list of all plugins, and lets you POST to add new plugins.'''
    @NAMESPACE.doc('list_plugins')
    @cross_origin(headers=["Access-Control-Allow-Origin", "*"])
    def get(self):
        '''Gets the list of plugins.'''
        session = SESSION()
        plugins_objects = session.query(
            Plugin)
        schema = PluginSchema(many=True)
        all_plugins = schema.dump(plugins_objects)

        session.close()
        return jsonify(all_plugins.data)

    @NAMESPACE.doc('create_plugin')
    @cross_origin(headers=["Content-Type", "Authorization"])
    @cross_origin(headers=["Access-Control-Allow-Origin", "*"])
    @requires_auth
    @NAMESPACE.doc(security='apikey')
    def post(self):
        '''Posts a new plugin.'''
        payload = NAMESPACE.apis[0].payload
        payload['user_id'] = get_user_id()
        posted_plugin = PluginSchema(
            only=('plugin_name',
                  'plugin_author_id',
                  'plugin_description')).load(payload)

        plugin = Plugin(**posted_plugin.data)

        session = SESSION()
        session.add(server)
        session.commit()

        new_plugin = PluginSchema().dump(plugin)
        session.close()
        return jsonify(new_plugin)
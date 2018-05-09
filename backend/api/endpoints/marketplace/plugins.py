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
from api.endpoints.marketplace import (NAMESPACE)
from api.endpoints.marketplace.plugin import (PLUGIN)

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
			Server)
		schema = PluginSchema(many=True)
		all_plugins = schema.dump(plugins_objects)

		session.close()
		return jsonify(all_plugins.data)

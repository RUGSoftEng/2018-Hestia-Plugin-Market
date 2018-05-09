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

)
from api.endpoints.marketplace import (NAMESPACE)
from api.endpoints.marketplace.plugin import (PLUGIN)

BASE.metadata.create_all(ENGINE)

@NAMESPACE.route('/')
class PluginList(Resource):
	'''Shows a list of all plugins, and lets you POST to add new plugins.'''
	@NAMESPACE.doc('list_plugins')
	@cross_origin(headers=["Content-Type", "Authorization"])
	@cross_origin(headers=["Access-Control-Allow-Origin", "*"])
	@requires_auth
	@NAMESPACE.doc(security='apikey')
	def get(self):
		'''Gets the list of plugins.'''
		session = SESSION()
		
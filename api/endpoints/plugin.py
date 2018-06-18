from flask_restplus import (
    Namespace,
    Resource,
)

"""
Endpoint for interacting with singular plugins.
"""

ns = Namespace(
    'plugin', description='List of all plugins available.')


@ns.route('/<string:id>')
@ns.response(404, 'Plugin not found.')
class PluginResource(Resource):
    #  Interaction with a specific plugin, specified by the unique id.

    @ns.doc('get_plugin')
    def get(self, id):
        return id

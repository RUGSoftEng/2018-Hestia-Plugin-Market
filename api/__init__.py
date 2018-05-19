"""
Create the API from the underlying endpoints.
"""
from flask_restplus import Api
from api.endpoints.servers.servers import NAMESPACE as SERVERS_NAMESPACE
from api.endpoints.users.users import NAMESPACE as USERS_NAMESPACE
from api.endpoints.marketplace import NAMESPACE as MARKETPLACE_NAMESPACE
from api.endpoints.marketplace.plugins.plugins import NAMESPACE as PLUGINS_NAMESPACE

AUTHORIZATIONS = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'authorization'
    }
}

API = Api(
    version='1.0',
    title='Hestia Plugin Marketplace API',
    description='The Hestia Plugin Marketplace API, providing plugins and their files.',
    authorizations=AUTHORIZATIONS
)


# Adds the SERVER and USER namespace to the API
API.add_namespace(PLUGINS_NAMESPACE)

"""
Create the API from the underlying endpoints.
"""

from flask_restplus import (Api)

from api.endpoints.plugins import (ns as PLUGINS_NAMESPACE)

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

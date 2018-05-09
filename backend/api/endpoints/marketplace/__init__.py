"""
Setup the API namespace for marketplace
"""
from flask_restplus import Namespace

NAMESPACE = Namespace(
    'marketplace', description='Area to add plugins to servers.')

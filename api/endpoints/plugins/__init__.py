"""
Setup the API namespace for plugins
"""
from flask_restplus import Namespace

NAMESPACE = Namespace(
    'plugins', description='List of all plugins available.')

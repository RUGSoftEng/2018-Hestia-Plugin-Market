"""
Setup the API namespace for marketplace
"""
from flask_restplus import Namespace

NAMESPACE = Namespace(
    'marketplace', description='A place to find and install plugins on the controller.')

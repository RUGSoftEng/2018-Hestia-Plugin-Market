"""
Declare the model objects for the database as well as schema for each
"""
from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from api.database.entities.entity import Entity, BASE
from api.database.util import url_safe_uuid


class User(Entity, BASE):
    """
    The user entity.
    """
    __tablename__ = 'users'

    user_id = Column(String, primary_key=True)
    servers = relationship("Server", cascade="all, delete-orphan")

    def __init__(self, user_id):
        Entity.__init__(self)
        self.user_id = user_id


class UserSchema(Schema):
    """
    The users schema.
    """
    user_id = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


"""
Table used to define many-to-many relationship between servers and plugins.
"""
plugin_server_association_table = Table('association', BASE.metadata,
    Column('plugin_id', String, ForeignKey('plugins.plugin_id')),
    Column('server_id', String, ForeignKey('servers.server_id'))
)


class Server(Entity, BASE):
    """
    The server entity.
    """
    __tablename__ = 'servers'

    server_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.user_id'))
    server_name = Column(String)
    server_address = Column(String)
    server_port = Column(String)

    plugins = relationship(
        "Plugin",
        secondary=plugin_server_association_table,
        back_populates="servers"
    )

    def __init__(self, user_id, server_name, server_address, server_port):
        Entity.__init__(self)
        self.server_id = url_safe_uuid()
        self.user_id = user_id
        self.server_name = server_name
        self.server_address = server_address
        self.server_port = server_port


class ServerSchema(Schema):
    """
    The server schema.
    """
    server_id = fields.Str()
    user_id = fields.Str()
    server_name = fields.Str()
    server_address = fields.Str()
    server_port = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class Plugin(Entity, BASE):
    """
    The plugin entity.
    """
    __tablename__ = 'plugins'

    plugin_id = Column(String, primary_key=True)
    plugin_name = Column(String, unique=True)
    plugin_author_id = Column(String, ForeignKey('users.user_id'))
    plugin_description = Column(String)
    plugin_votes = Column(Integer)

    servers = relationship(
        "Server", 
        secondary=plugin_server_association_table,
        back_populates="plugins"
    )

    def __init__(
        self,
        plugin_name, 
        plugin_author_id, 
        plugin_description):
        Entity.__init__(self)
        self.plugin_id = url_safe_uuid()
        self.plugin_name = plugin_name
        self.plugin_author_id = plugin_author_id
        self.plugin_description = plugin_description
        self.plugin_votes = 0


class PluginSchema(Schema):
    """
    The plugin schema.
    """
    plugin_id = fields.Str()
    plugin_name = fields.Str()
    plugin_author_id = fields.Str()
    plugin_description = fields.Str()
    plugin_votes = fields.Int()

    created_at = fields.DateTime()
    updated_at = fields.DateTime()
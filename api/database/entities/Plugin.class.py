"""
Plugin Object

Represents a plugin, with some metadata.
"""

from datetime import datetime

from sqlalchemy import Column, String, Date, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from api.database.tables import plugin_tag_association_table
from api.database.util import url_safe_uuid


class Plugin(declarative_base()):

    __tablename__ = 'plugins'

    # The unique identifier for this plugin.
    id = Column(String, primary_key=True)
    # The unique name of the plugin.
    name = Column(String(length=100), nullable=False, unique=True)
    # The id of the author of the plugin.
    author_id = Column(String, nullable=False)
    # The date on which this plugin was created.
    created_date = Column(Date, nullable=False)
    # The date on which this plugin was most recently updated, either with new files or new metadata.
    last_edited_date = Column(Date, nullable=False)
    # The version of the plugin, specified by the author.
    version = Column(String(length=20), nullable=True)
    # A short description of the plugin.
    description_short = Column(Text(length=144), nullable=True)
    # A longer, more verbose description of the plugin.
    description_long = Column(Text, nullable=True)
    # The number of positive votes for a plugin.
    up_goats = Column(Integer, nullable=False)
    # The number of negative votes for a plugin.
    down_goats = Column(Integer, nullable=False)
    # One or more tags which give the plugin some meaning.
    tags = relationship("Tag",
                        secondary=plugin_tag_association_table,
                        back_populates='plugins')

    def __init__(self, name, author_id, version, description_short, description_long):
        self.name = name
        self.author_id = author_id
        self.version = version
        self.description_short = description_short
        self.description_long = description_long

        self.id = url_safe_uuid()  # Set the id to a unique string.
        self.created_date = datetime.now()  # Since we initialize the plugin now, it is created now.
        self.last_edited_date = datetime.now()  # When created, edited date is same as created date.
        self.up_goats = 0  # Initially, there are zero up_goats.
        self.down_goats = 0  # Initially, there are also zero down_goats.

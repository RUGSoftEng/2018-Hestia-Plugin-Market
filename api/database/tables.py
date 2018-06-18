"""
Tables file.

This file holds all tables defined for the database which cannot be defined with an object.
"""

from sqlalchemy import (
    Table,
    Column,
    String,
    ForeignKey,
)
from sqlalchemy.ext.declarative import (declarative_base)

# This table defines a many-to-many relationship between tags and plugins.
PLUGIN_TAG_ASSOCIATION_TABLE = Table(
    'association',
    declarative_base().metadata,
    Column('plugin_id', String, ForeignKey('plugins.id')),
    Column('tag_name', String(40), ForeignKey('tags.name'))
)

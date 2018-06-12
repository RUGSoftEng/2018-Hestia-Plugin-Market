"""
Tag object

Represents a tag which can be applied to one or more plugins, giving it some subject meaning.
"""

from sqlalchemy import (
    Column,
    String,
    Text,
)
from sqlalchemy.ext.declarative import (declarative_base)
from sqlalchemy.orm import (relationship)

from api.database.tables import (PLUGIN_TAG_ASSOCIATION_TABLE)


class Tag(declarative_base()):
    """
    The model for a tag. A tag provides additional metadata for a plugin to
    provide it additional (searchable) context.
    """

    __tablename__ = 'tags'

    # The unique name of a tag.
    name = Column(String(40), primary_key=True)
    # The description of a tag's meaning.
    description = Column(Text, nullable=True)
    # The relationship to plugin_tag table for many-to-many.
    plugins = relationship('Plugin',
                           secondary=PLUGIN_TAG_ASSOCIATION_TABLE,
                           back_populates='tags')

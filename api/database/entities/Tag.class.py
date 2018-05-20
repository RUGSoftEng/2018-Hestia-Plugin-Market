"""
Tag object

Represents a tag which can be applied to one or more plugins, giving it some subject meaning.
"""
from sqlalchemy import Column, String, Text
from sqlalchemy.ext.declarative import declarative_base


class Tag(declarative_base()):

    __tablename__ = 'tags'

    # The unique name of a tag.
    name = Column(String(40), primary_key=True)
    # The description of a tag's meaning.
    description = Column(Text, nullable=True)

"""
Vote Object

This represents a vote (up_goat or down_goat) cast by a user for a plugin.
"""
from sqlalchemy import Column, String, Integer, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base


class UserVote(declarative_base()):

    __tablename__ = 'uservotes'

    # The user's unique id.
    user_id = Column(String, nullable=False)
    # The plugin's unique id.
    plugin_id = Column(String, nullable=False)
    # Either 1 for positive, or -1 for negative vote.
    vote = Column(Integer, CheckConstraint('vote = 1 OR vote = -1'), nullable=False)

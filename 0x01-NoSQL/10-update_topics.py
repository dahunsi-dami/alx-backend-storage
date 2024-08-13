#!/usr/bin/env python3
"""Module containing update_topics function."""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document
    based on the name.

    Args:
        mongo_collection: the pymongo object
        name (string): the school name to update.
        topics (list of strings): list of topics.

    Returns:
        nothing.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

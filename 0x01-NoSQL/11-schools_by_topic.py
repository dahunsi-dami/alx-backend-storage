#!/usr/bin/env python3
"""Module for schools_by_topic function."""


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Returns list of schools w/ a specific topic.

    Args:
        mongo_collection: the pymongo object
        topic (string): to be topic searched.

    Returns:
        list of schools w/ the specific topic.
    """
    schls = []
    for schl in mongo_collection.find({"topics": topic}):
        schls.append(schl)
    return schls

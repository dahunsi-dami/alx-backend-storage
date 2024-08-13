#!/usr/bin/env python3
"""Module containing insert_school function."""


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts new doc, based on kwargs, in a collection.

    Args:
        mongo_collection: the pymongo object
        kwargs: keyword args to be inserted as docs.

    Returns:
        the new _id of inserted doc(s).
    """
    newdoc = mongo_collection.insert_one(kwargs)
    return newdoc.inserted_id

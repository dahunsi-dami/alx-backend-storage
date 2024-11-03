#!/usr/bin/env python3
"""Module to calculate average score for each student."""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Args:
        mongo_collection: the pymongo collection object for students.

    Returns:
        all students sorted by average score.
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                    }
                }
            },
        {
            "$sort": {
                "averageScore": -1
                }
            }
            ]

    return list(mongo_collection.aggregate(pipeline))

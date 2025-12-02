#!/usr/bin/env python3
"""
Function that changes all topics of a school document based on the name
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of a school document identified by its name.

    Args:
        mongo_collection: pymongo collection object
        name (str): name of the school to update
        topics (list of str): list of topics to set
    """
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    print("OK")

#!/usr/bin/env python3
"""
Function that inserts a new document in a collection
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in the specified MongoDB collection

    Args:
        mongo_collection: pymongo collection object
        **kwargs: key-value pairs representing fields of the new document

    Returns:
        The _id of the newly inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

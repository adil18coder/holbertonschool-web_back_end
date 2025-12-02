#!/usr/bin/env python3
"""
Function that lists all documents in a collection
"""

def list_all(mongo_collection):
    """
    List all documents in the specified MongoDB collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        list of documents, or empty list if no documents
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())

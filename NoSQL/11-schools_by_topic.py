#!/usr/bin/env python3
"""
Function that returns the list of schools having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Finds all documents where the 'topics' list contains the specified topic

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for

    Returns:
        List of matching documents
    """
    if mongo_collection is None or topic is None:
        return []

    return list(mongo_collection.find({"topics": topic}))

#!/usr/bin/env python3
"""9. Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs

    Param:
        mongo_collection (Collection): pymongo collection
        kwargs (dict): Document
    Return:
        ObjectId: the id of the created collection
    """
    _id = mongo_collection.insert_one(kwargs).inserted_id

    return _id

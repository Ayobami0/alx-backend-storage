#!/usr/bin/env python3
"""8. List all documents in Python"""


def list_all(mongo_collection):
    """lists all documents in a collection

    Param:
        mongo_collection (pymongo): pymongo collection object
    Return:
        None: None
    """
    _list = mongo_collection.find()
    if mongo_collection.count_documents({}) == 0:
        return []
    return list(_list)

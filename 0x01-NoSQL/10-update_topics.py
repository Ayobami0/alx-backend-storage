#!/usr/bin/env python3
"""10. Change school topics"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics associated with a given name in a MongoDB collection.

    Args:
      mongo_collection (pymongo.collection.Collection): A reference to a
          MongoDB collection object.
      name (str): The name for which to update the topics.
      topics (list): A list of strings representing the new topics.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

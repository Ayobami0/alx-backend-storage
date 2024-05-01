#!/usr/bin/env python3
"""11. Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """Filters and retrieves schools based on a specified topic
    from a MongoDB collection.

    Params:
      mongo_collection (pymongo.collection.Collection): A reference
        to a MongoDB collection object containing school data.
      topic (str): The topic to filter by. Schools with this
        topic in their list will be returned.

    Returns:
      list: A list of dictionaries representing the filtered schools.
        Each dictionary contains document information from the
        MongoDB collection, including
        `_id` (if available), `name`, and `topics`.
    """
    schools = mongo_collection.find({"topics": topic})

    return list(schools)

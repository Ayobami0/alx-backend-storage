#!/usr/bin/env python3
"""14. Top students"""


def top_students(mongo_collection):
    """
    Retrieves schools with their average topic scores
        from a MongoDB collection.

    Params:
      mongo_collection (pymongo.collection.Collection): A reference
        to a MongoDB collection containing
        school data with a 'topics' field containing score information.

    Returns:
      cursor: A pymongo cursor object containing
      the filtered and sorted school documents.
             Each document includes `_id` (if available), `name`, and
             a calculated `averageScore` field representing
             the average score within the `topics` list.

    Raises:
      pymongo.errors.PyMongoError: If an error occurs while
      interacting with the MongoDB collection.
    """
    return mongo_collection.find(
        {},
        {
            "name": 1,
            "averageScore": {
                "$avg": "$topics.score",
            },
        },
    ).sort({"averageScore": -1})

#!/usr/bin/env python3
"""14. Top students"""


def top_students(mongo_collection):
    return mongo_collection.find(
        {},
        {
            "name": 1,
            "averageScore": {
                "$avg": "$topics.score",
            },
        },
    ).sort({"averageScore": -1})

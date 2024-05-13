#!/usr/bin/env python3
""" Top students  """
import pymongo


def top_students(mongo_collection):
    """ Average top students

        Args:
            mongo_collection: Collection to find avg top

        Return:
            List all top students
    """
    top_students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_students
"""
Biqing Qiu
bq2134
Script to work with MongoDB
In Python
My Genre is Short
"""
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.hw3

#Find all movies in genre "Short" that is "NOT RATED" 
#and change rating to "Pending rating"
#operation must be in-place and atomic at document-level

db.movies.update_one(
{and: ["genres": "Short"},{"rated": "NOT RATED"}]},
{"$set": {"rated": "Pending rating"}}
)


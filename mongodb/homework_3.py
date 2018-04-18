"""
Biqing Qiu
bq2134
Script to work with MongoDB
In Python
My Genre is Short
"""
import pymongo
from pymongo import MongoClient
from pprint import pprint

db = MongoClient("mongodb://localhost").hw3

#Part A
#Find all movies in genre "Short" that is "NOT RATED" 
#and change rating to "Pending rating"
#operation must be in-place and atomic at document-level

db.movies.update_many(
{"genres": "Short","rated": "NOT RATED"},{"$set": {"rated": "Pending rating"}})

#Part b
#Insert movie from IMDB into database from my genre
db.movies.insert_one(
{
	"title":"Pandas",
	"year":2018,
	"countries":["USA"],
	"genres":["Short", "Documentary"],
	"directors":["David Douglas", "Drew Fellman"],
	"imdb":{
		"id":12345,
		"rating":7.4,
		"votes":40
	}	
})

#Part c
#Use aggregation to find no. of movies in my genre
#ie. Short
cursor1 = db.movies.aggregate(
[{"$match":{"genres": "Short"}},
{"$group": {"_id": "Short", "count": {"$sum":1}}}
])
for document in cursor1:
	pprint(document)

#Part d
#Use aggregation to find no. of movies in my birth country
# ie. USA
# with rated = Pending rating
cursor2 = db.movies.aggregate(
[{"$match":{"countries": "USA"}},
{"$match": {"rated": "Pending rating"}},
{"$group": {"_id": {"country": "USA", "rated": "Pending rating"}, "count": {"$sum":1}}}
])
for document in cursor2:
	pprint(document)

#Part e
#Make 2 collections and join with $lookup
#first make an extra collection
db.avant_garde.insert_one(
{
	"title":"Pandas",
	"food": "bamboo",
	"fur": "black and white"	
})

db.avant_garde.insert_one(
{
	"title":"Night and Fog",
	"food": "water",
	"fur": "night and fog"
})

db.avant_garde.insert_one(
{
	"title":"Zero for Conduct",
	"food": "guns and roses",
	"fur": "pelt"
})	

pipeline = [
{"$lookup":{
    "from": "movies",
    "localField": "title",
    "foreignField": "title",
    "as": "name"}}]

for doc in (db.avant_garde.aggregate(pipeline)):
    pprint (doc)




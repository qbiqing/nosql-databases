# Script to add users and objects
# Biqing Qiu
# bq2134

import pymongo
from pymongo import MongoClient
from pprint import pprint

db = MongoClient("mongodb://localhost").finalproj

# Insert users 1, 2, 3
db.Users.insert_one({
	"id":"user1", 
	"commented":[], 
	"posted":["article1", "article4", "article5", "article6"], 
	"voted": []}
)

db.Users.insert_one({
	"id":"user2", 
	"commented":["article1"], 
	"posted":["article2", "article7", "article8", "article9", "article10"], 
	"voted": ["article1"]}
)

db.Users.insert_one({
	"id":"user3", 
	"commented":["article1", "article2"], 
	"posted":["article3", "article11", "article12", "article13", "article14", "article15"], 
	"voted": ["article1","article2"]}
)

db.Articles.insert_one( 
	{
	"articleid": "article1", 
	"title": "what is mongodb", 
	"link":"#", 
	"poster": "user1", 
	"time":"2018-06-19",
	"votesno": 2,
	"votes": ["user2", "user3"], 
	"commentsno": 2, 
	"comments":[{
			"userid":"user2", 
			"comment": "hi"},
		{
			"userid":"user3", 
			"comment": "hello"}
		]
	}
)

db.Articles.insert_one( 
	{
	"articleid": "article2", 
	"title": "what is neo4j", 
	"link":"#", 
	"poster": "user2", 
	"time":"2018-06-19",
	"votesno": 1,
	"votes": ["user3"], 
	"commentsno": 1, 
	"comments":[
		{
			"userid":"user3", 
			"comment": "hello"}
		]
	}
)

db.Articles.insert_one( 
	{
	"articleid": "article3", 
	"title": "what is redis", 
	"link":"#", 
	"poster": "user3", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)

db.Articles.insert_one( 
	{
	"articleid": "article4", 
	"title": "what is ghost", 
	"link":"#", 
	"poster": "user1", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)

db.Articles.insert_one( 
	{
	"articleid": "article5", 
	"title": "what is jon snow", 
	"link":"#", 
	"poster": "user1", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)


db.Articles.insert_one( 
	{
	"articleid": "article6", 
	"title": "what is snow white", 
	"link":"#", 
	"poster": "user1", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)

db.Articles.insert_one( 
	{
	"articleid": "article7", 
	"title": "what is web", 
	"link":"#", 
	"poster": "user2", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)


db.Articles.insert_one( 
	{
	"articleid": "article8", 
	"title": "what is a duck", 
	"link":"#", 
	"poster": "user2", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)


db.Articles.insert_one( 
	{
	"articleid": "article9", 
	"title": "what is donald", 
	"link":"#", 
	"poster": "user2", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)

db.Articles.insert_one( 
	{
	"articleid": "article10", 
	"title": "what is trump", 
	"link":"#", 
	"poster": "user2", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)

db.Articles.insert_one( 
	{
	"articleid": "article11", 
	"title": "what is redistribution", 
	"link":"#", 
	"poster": "user3", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)

db.Articles.insert_one( 
	{
	"articleid": "article12", 
	"title": "what is equality", 
	"link":"#", 
	"poster": "user3", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)
db.Articles.insert_one( 
	{
	"articleid": "article13", 
	"title": "what is communism", 
	"link":"#", 
	"poster": "user3", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)

db.Articles.insert_one( 
	{
	"articleid": "article14", 
	"title": "what is lenin", 
	"link":"#", 
	"poster": "user3", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)

db.Articles.insert_one( 
	{
	"articleid": "article15", 
	"title": "what is stalin", 
	"link":"#", 
	"poster": "user3", 
	"time":"2018-06-19",
	"votesno": 0,
	"votes": [], 
	"commentsno": 0, 
	"comments":[]
	}
)












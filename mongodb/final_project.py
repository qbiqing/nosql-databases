# Put the use case you chose here. Then justify your database choice:
# I chose the use case Hacker News. I chose mongodb because I can keep both Users and Articles 
# as collections, and individual users and articles as documents within each collection.
# I find it a neat way of organizing information, and keeping track of records such as
# the articles that a user has posted, commented on or upvoted, and the number of votes
# and comments on each article.
#
# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.
# If one server of the cluster goes down, if the server is the primary server, a request will be 
# sent to one of the read replicas in the cluster. One of the replicas (secondary servers) can then 
# take over the primary server and continue the work on the database.
#
# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?
# You cannot lose information about your user as if that happens, the user will not be able to log back
# on the platform. You also cannot lose basic information (title, link) of each article that a user posts. 
# To mitigate the risk of lost data, one can create a replica collection for Users, such as UsersBackup, 
# so that if one collection is breached, you still have another collection of the same information. 
# The replica collections can be created at the same time as creating the original collections 
# (ie. on command line).
#


import pymongo
from pymongo import MongoClient
from pprint import pprint

db = MongoClient("mongodb://localhost").finalproj
# Action 1: User posts an article
db.Articles.insert_one(
{
	"articleid": "article16", 
	"title": "what is mao", 
	"link":"#", 
	"poster": "user1", 
	"time":"2018-08-19",
	"votesno": "0",
	"votes": [], 
	"commentsno": "0", 
	"comments":[]
	}
)
db.Users.update(
	{"id": "user1"},
	{"$push":{"posted": "article16"} }
)

# Action 2: Display list of top 3 articles based on votes
cursor1 = db.Articles.aggregate(
[{"$sort":{"votesno": {"$meta": "textScore"}}},
{"$limit": 3}
])
for document in cursor1:
	pprint(document)

# Action 3: User upvotes an article
db.Users.update(
	{"id": "user1"},
	{"$push":{"voted": "article16"} }
)
db.Articles.update(
	{"articleid": "article16"},
	{"$push":{"votes": "user1"} }, 
	{"$inc": {"votesno":"1"}}
)

# Action 4: User comments on article
db.Users.update(
	{"id": "user1"},
	{"$push":{"commented": "article15"} }
)
db.Articles.update(
	{"articleid": "article15"},
	{"$push":{"comments": {"user1", "hi"}} },
	{"$inc": {"commentsno": "1"}}
)

# Action 5: User edits the title, link of an article posted
db.Articles.update(
	{"articleid": "article14"},
	{"$set":{"title": "what is life"}}
)

# Action 6: User removes an article
db.Articles.remove({"articleid": "article13"})
db.Users.update(
	{"id": "user3"},
	{"$pull":{"posted": "article13"} })

#find a list of people who commented on the removed article
commenters = []
cursor2 = db.Users.find({"commented": "article13"})
for document in cursor2:
	commenters.append(document.id)
for commenter in commenters:
	db.Users.update(
		{"id": commenter},
		{"$pull":{"commented": "article13"} })

#find a list of people who voted on the removed article
voters = []
cursor3 = db.Users.find({"voted": "article13"})
for document in cursor3:
	voters.append(document.id)
for voter in voters:
	db.Users.update(
		{"id": voter},
		{"$pull":{"voted": "article13"} })


# Action 7: User removes a vote
db.Articles.update(
	{"articleid": "article1"},
	{"$inc":{"votesno": "-1"}},
	{"$pull": {"votes": "user2"}}
)
db.Users.update(
	{"id": "user2"},
	{"$pull":{"voted": "article1"} })

# Action 8: User removes a comment
db.Articles.update(
	{"articleid": "article1"},
	{"$inc":{"commentsno": "-1"}},
	{"$pull": {"comments": "user2"}}
)
db.Users.update(
	{"id": "user2"},
	{"$pull":{"commented": "article1"} })


















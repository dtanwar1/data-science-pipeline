import utils.mongo_db_client as mdc
import datetime
from bson.objectid import ObjectId
import utils.comment_analyser as  cma

s3 = 0
s3c =0
threshold = 10

youtube_collection = mdc.getCollection("kek_db", "twitter")
totalCount=0
startDate = datetime.datetime(2022,11,4)
for i in range(0,42):
    s3 =0
    s3c = 0
    query_date = ObjectId.from_datetime(startDate + datetime.timedelta(days=i))
    for col in youtube_collection.find({"_id":{"$gte": query_date}}).limit(threshold):
        s3 += cma.analyseComment(col["tweet_text"])
        s3c +=1
    mdc.insert(
        {
            "date" : query_date,
            "avgScore":s3/s3c
        },"twtTox",False
    )    
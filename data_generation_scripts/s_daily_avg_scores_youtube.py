from textblob import TextBlob
import sys
import utils.mongo_db_client as mdc
import datetime
from bson.objectid import ObjectId


s3 = 0
s3c =0

youtube_collection = mdc.getCollection("kek_db", "youtube")
startTime = None
count = 0
x_axis = []
y_axis = []
totalCount=0
for col in youtube_collection.find():
    if not startTime:
        startTime = col['_id'].generation_time 
    endTime = col['_id'].generation_time  
    sub = TextBlob(col["snippet"]["description"]) 
    s3 += sub.subjectivity    
    s3c += 1
    totalCount += 1
    if(startTime.strftime("%d/") != endTime.strftime("%d/")):    
        startTime = endTime
        mdc.insert({
            "date" : ObjectId.from_datetime(startTime),
            "avgScore":s3/s3c
        }, 'ytSentiment', False)
        s3 = 0
        s3c = 0
print(totalCount)        

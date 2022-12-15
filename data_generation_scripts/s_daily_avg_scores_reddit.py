from textblob import TextBlob
import utils.mongo_db_client as mdc
from bson.objectid import ObjectId


s3 = 0
s3c =0

reddit_collection = mdc.getCollection("kek_db", "reddit")
startTime = None
count = 0
x_axis = []
y_axis = []
totalCount=0
for col in reddit_collection.find():
    if not startTime:
        startTime = col['_id'].generation_time 
    endTime = col['_id'].generation_time  
    sub = TextBlob(col["Comment"]) 
    s3 += sub.subjectivity    
    s3c += 1
    totalCount += 1
    if(startTime.strftime("%d/") != endTime.strftime("%d/")):    
        startTime = endTime
        mdc.insert({
            "date" : ObjectId.from_datetime(startTime),
            "avgScore":s3/s3c
        }, 'rdSentiment', False)
        s3 = 0
        s3c = 0
print(totalCount)        

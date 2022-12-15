import utils.mongo_db_client as mdc
import datetime
import math
from flask import Flask,render_template,request
from bson.objectid import ObjectId


app = Flask(__name__)

@app.route("/")

def home():
    ag = mdc.getCollection("kek_db", "data_aggregates")
    val = ag.find_one({"param" : "totalDataC"})
    return render_template("index.html", tc=str(math.floor(val["value"]/1000000)) + str("M"))

@app.route("/senti/data")
def getSentiData():
    args = request.args
    start_date = args["sd"]
    end_date = args["ed"]
    s1=0
    s1c = 0
    s2=0
    s2c = 0
    s3 = 0
    s3c =0
    dates= []
    start_date = ObjectId.from_datetime(datetime.datetime.strptime( start_date,"%m/%d/%Y" ))
    end_date = ObjectId.from_datetime(datetime.datetime.strptime( end_date,"%m/%d/%Y" ))
    reddit_collection = mdc.getCollection("kek_db", "rdSentiment")
    twitter_collection = mdc.getCollection("kek_db", "twtSentiment")
    yts_col = mdc.getCollection("kek_db", "ytSentiment")
    
    for col in reddit_collection.find({"date": {"$gte": start_date, "$lte": end_date}}):
        sub = col["avgScore"]
        s1 += sub
        s1c +=1
    for col in twitter_collection.find({"date": {"$gte": start_date, "$lte": end_date}}):
        sub = col["avgScore"]
        s2 += sub
        s2c += 1
    for col in yts_col.find({"date": {"$gte": start_date, "$lte": end_date}}):
        s3 += col["avgScore"]
        s3c += 1
        dates.append(ObjectId(col["date"]).generation_time.strftime("%m/%d/%Y"))
    subjectives = [s1/s1c, s2/s2c, s3/s3c]
    return render_template("subject.html",sub = subjectives)


@app.route("/toxi/data/l")
def getToxiDatal():
    args = request.args
    start_date = args["sd"]
    end_date = args["ed"]
    dates= []
    start_date = ObjectId.from_datetime(datetime.datetime.strptime( start_date,"%m/%d/%Y" ))
    end_date = ObjectId.from_datetime(datetime.datetime.strptime( end_date,"%m/%d/%Y" ))
    reddit_collection = mdc.getCollection("kek_db", "rdTox")
    twitter_collection = mdc.getCollection("kek_db", "twtTox")
    yts_col = mdc.getCollection("kek_db", "ytTox")
    tox_r =[]
    tox_t = []
    tox_y = []
    for col in reddit_collection.find({"date": {"$gte": start_date, "$lte": end_date}}):
        tox_r.append(col["avgScore"])
    for col in twitter_collection.find({"date": {"$gte": start_date, "$lte": end_date}}):
        tox_t.append(col["avgScore"])
    for col in yts_col.find({"date": {"$gte": start_date, "$lte": end_date}}):
        tox_y.append(col["avgScore"])
        dates.append(ObjectId(col["date"]).generation_time.strftime("%m/%d/%Y"))
    return render_template("toxicity_l.html",tox_y = tox_y, tox_r = tox_r, tox_t = tox_t, dates = dates) 

@app.route("/toxi/data/p")
def getToxiDatap():
    args = request.args
    start_date = args["sd"]
    end_date = args["ed"]
    dates= []
    start_date = ObjectId.from_datetime(datetime.datetime.strptime( start_date,"%m/%d/%Y" ))
    end_date = ObjectId.from_datetime(datetime.datetime.strptime( end_date,"%m/%d/%Y" ))
    reddit_collection = mdc.getCollection("kek_db", "rdTox")
    twitter_collection = mdc.getCollection("kek_db", "twtTox")
    yts_col = mdc.getCollection("kek_db", "ytTox")
    tox_r =[]
    tox_t = []
    tox_y = []
    for col in reddit_collection.find({"date": {"$gte": start_date, "$lte": end_date}}):
        tox_r.append(col["avgScore"])
    for col in twitter_collection.find({"date": {"$gte": start_date, "$lte": end_date}}):
        tox_t.append(col["avgScore"])
    for col in yts_col.find({"date": {"$gte": start_date, "$lte": end_date}}):
        tox_y.append(col["avgScore"])
        dates.append(ObjectId(col["date"]).generation_time.strftime("%m/%d/%Y"))
    return render_template("toxicity_p.html",tox_y = tox_y, tox_r = tox_r, tox_t = tox_t, dates = dates)        

if __name__ == "__main__":
    app.run(port=8006, debug=True, host="0.0.0.0")    

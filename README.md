# project-2-implementation-kekology

## Project Abstract
This project is aimed at represeting the analytics on data collected collected using the data collection system as part of project 1

The advent of the Internet has given rise to a number of important innovations that drive the human race forward connection being one of the most important ones of all. Over the past few decades, the Internet has provided a number of platforms to individuals and groups alike to share their views and ideologies. Oftentimes this is for the better, after all, it’s the collective thought that pushes the boundaries of any domain. But there also exists another side to the same coin. One, that has quickly risen among a niche populace and has been rapidly gaining momentum. The very idea of free speech coupled with anonymity over the internet has enabled a certain sect of internet users to spread hate, misogyny and abhorement towards other classes, mainly through various Social Media platforms. This has led to a number of problems that the general populace faces either directly or through the actions of others. Depression, anxiety, suicides are just the general trends that are seen among people who have faced some form of abuse or hatred online. Another worrying aspect to this trend is that the current generation (GenZ) is quickly gravitating towards these unwanted elements and generally dismiss the morality of a situation. This paper provides an abstract proposal on the collection of various data sources to study the general trend and the growing idea about hatred on the internet among the popular platforms that usually form the gut of online hatred, namely, Reddit, Twitter and Youtube (video descriptions). This representation also outlines the average toxicity scores across platforms and help us to get an understanding of which platform is more toxic bottle down to the averages on specific date ranges as well 

## Team - Kekology

* Abhishek Satpute, asatpute1@binghamton.edu
* Deepak Tanwar, dtanwar1@binghamton.edu
* Vaibhav Gohil, vgohil1@binghamton.edu
* Neha Patil, npatil9@binghamton.edu
* Venkat Sujit Adabala vadabal1@binghamton.edu

## Tech-stack

* `python` - The project is developed and tested using python v3.8. [Python Website](https://www.python.org/)
* `flask` - https://flask.palletsprojects.com/en/2.2.x/
* `request` - Request is a popular HTTP networking module(aka library) for python programming language. [Request Website](https://docs.python-requests.org/en/latest/#)
* `Mongo db`- This project uses nosql database for saving collected data and also uses the pymongo tool to retreive data using queries. 
* [MongoDB Website](https://www.mongodb.com/cloud/atlas)
* [Python Mongo Adapter - pymongo](https://pymongo.readthedocs.io/en/stable)
* [Text Blob for sentiment analysis] (https://textblob.readthedocs.io/en/dev/quickstart.html)
* [Perspective API for toxicity analysis] (https://perspectiveapi.com/) 
* [Library Used for plotting] chart.js (https://www.chartjs.org/)

## Steps To Run
# web app
    pip3 install -r requirements.txt
    python3 main.py (in root folder, this will start flask development server on port 8006)
# data generation scrips for pre computing toxicity and subjectivity
    cd data_generation_scripts
    nohup {script_name}  -  script names start with t for toxicity calculations , s for subjectivity     calculations and for toxicity configuration we can limit the of tweets being analysed and form which date to not to over head the toxicity api endpoint, can be chaged using the top most variables in the script

## Database schema - NoSQL

```bash

twtTox
{
    "_id" : Object,
    "date": Datetime ObjectId,
    "avgScore" : Integer
}

rdTox
{
    "_id" : Object,
    "date": Datetime ObjectId,
    "avgScore" : Integer
}

ytTox
{
    "_id" : Object,
    "date": Datetime ObjectId,
    "avgScore" : Integer
}

twtSentiment
{
    "_id" : Object,
    "date": Datetime ObjectId,
    "avgScore" : Integer
}

ytSentiment
{
    "_id" : Object,
    "date": Datetime ObjectId,
    "avgScore" : Integer
}

twtSentiment
{
    "_id" : Object,
    "date": Datetime ObjectId,
    "avgScore" : Integer
}


 twitter
{
  "_id": Object,
  "tweet_id": Integer,
  "tweet_text": String,
  "tweet_retweets": Integer,
  "tweet_no_of_replies":Integer,
  "createdDTTM":DateTime
}

youtube
{
   "_id":{
      "$oid":String
   },
  "id":String,
  "snippet":{
      "publishedAt":DateTime,
      "channelId":String,
      "title":String,
      "description":String,         
      },
  "tags": List<String>,
  "categoryId":String,
  "defaultLanguage":String
  "contentDetails":{
    "duration":String
  },
  "statistics":{
    "viewCount":Integer,
    "likeCount":Integer,
    "favoriteCount":Integer,
    "commentCount":Integer
  }
}

reditt
{
    "_id":ObjectId  
    "id": string,
    "text": string,
    "kind": string,
    "subreddit_id": string,
}
reditt_politics
{
    "_id":ObjectId  
    "id": string,
    "text": string,
    "kind": string,
    "subreddit_id": string,
}
```

## Special instructions 
Recommended to use nohup for datageneration scripts as it might take couple of minutes to generate data and in the comment analyser under data_generation_scripts/utils/comment_analyser.py
#Import the necessary methods from tweepy library

import sys

from tweepy import  StreamListener

from tweepy import OAuthHandler

from tweepy import Stream

from pymongo import MongoClient

import json

import pymongo

import time
import os

import csv

#Variables that contains the user credentials to access Twitter API 

API_KEY = 'rixFqBl7KY4W9p3h75AcJU5I2'

API_SECRET = '2d3AiWbD87PWPT7gM5SLeBstGDc1HR788o6eAMhdJeiwKhrYSs'

API_ACCESS_TOKEN = '2925273723-xvMbf58JbH5IjGZM1SYmiRoEkT8rF6OCDBhSxDr' 

API_ACCESS_SECRET = 'MDnPc0s4QdqiJjAWCHxioYN7joei7TagbkhDbo3GfGRFA'

start_time = time.time() #grabs the system time

class StdOutListener(StreamListener):
    def __init__(self, start_time = time.time(), time_limit=60):

        self.time = start_time
        self.limit = time_limit

    def on_data(self, raw_data):

        # data = json.loads(raw_data)

        # blizzard_collection.insert(data)

        #print ("Im executing")
        while (time.time() - self.time) < self.limit:

            try:

                client = MongoClient('localhost', 27017)
                db = client[sys.argv[2]]
                collection = db.twitter_collection
                tweet = json.loads(raw_data)
                collection.insert(tweet)
                tweets_iterator = collection.find()
                for tweet in tweets_iterator:
                    print (tweet['text'])
                return True
            except BaseException:
                print ('failed ondata,', str(e))
                time.sleep(5)
                pass
        exit()
    def on_status(self, status):

         # Prints the text of the tweet

        print('Tweet text: ' + status.text)
        # tweets_iterator = collection.find()
        # for tweet in tweets_iterator:
        #     print (tweet['text'])

        return True

    def on_error(self, status):

        print("status w/ this error %s" %status)

        client.close()

        return True

    def on_timeout(self):

        print('Timeout...')

        return True # To continue listening

if __name__ == '__main__':

    l = StdOutListener()

    auth = OAuthHandler(API_KEY, API_SECRET)

    auth.set_access_token(API_ACCESS_TOKEN, API_ACCESS_SECRET)

    stream = Stream(auth, l)

    x = list(csv.reader([sys.argv[1]]))[0]

    loc = [float(i) for i in x]
    stream.filter(locations=loc, 

        languages=['en'], async=False)
    


#Import the necessary package to process data in JSON format
import json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '367437965-UHlGKsxK2WfYNptu2tOPBgT7jxgFvSwJ5fuS59C3'
ACCESS_SECRET = 'qYJQdSzBfdNMPllmA5jU5xJAuyTGxzEs6G7uKRoENRsSu'
CONSUMER_KEY = 'n9j2KmkV3FFWkzgGeq4XdPWCp'
CONSUMER_SECRET = 'TszufpKDVtR9rkEkfBS8SdljhqMuxO26ohnUqqDjfTNk2xvJrx'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
#iterator = twitter_stream.statuses.sample()
#iterator = twitter_stream.statuses.filter(track="Google",language="en")
iterator = twitter_stream.statuses.filter(track="sleep,insomnia,cantsleep,melatonin,Ambien,zolpidem,edluar,intermezzo,lunesta,#insomnia,#cantsleep", language="en")

count = 0

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
for tweet in iterator:
	#tweet_count -= 1
	# Twitter Python Tool wraps the data returned by Twitter 
	# as a TwitterDictResponse object.
	# We convert it back to the JSON format to print/score
	t = json.dumps(tweet)
	count +=1
	print(count)

	with open('tweets.txt','a') as file:

		json.dump(t,file)  
		file.write("\n\n\n")  
	# The command below will do pretty printing for JSON data, try it out
	# print json.dumps(tweet, indent=4)
       
	#if tweet_count <= 0:
	#    break 
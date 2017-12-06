
#Import the necessary package to process data in JSON format
import json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '367437965-btxAYZqGUY4SY7pL5CYSJKk2pnOCfPtwKvyzyzJm'
ACCESS_SECRET = 'ONDV9zZDU1c7br0sInYJxQEvbZK5j5QzpKlixUA0MHAj4'
CONSUMER_KEY = 'U83tF3RvxLgQQsOh62sqfm2Md'
CONSUMER_SECRET = 'nwE9DbFt8f2UHPb8jqIrsbIcQeaDgyUxv1nNvggvAwr6Rmv1ty'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)


# Search for latest tweets"
iterator = twitter.search.tweets(q='sleep OR insomnia',count = 100)
print (str(len(iterator["statuses"])))

# Save each tweet in  a document called 'tweets.txt'
#for tweet in iterator:
	
	# We convert it to the JSON format 
t = json.dumps(iterator)
	
with open("tweetsSearch.json",'a') as file:

	json.dump(iterator,file)
	#	file.write("\n\n\n")


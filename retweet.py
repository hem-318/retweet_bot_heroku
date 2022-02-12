import tweepy
import os
from random import randint
from time import sleep
from dotenv import load_dotenv
load_dotenv()
#Accessing credentials from .env file
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")
search_keyword = os.getenv("search_keyword")
sleep_time = int(os.getenv("sleep_time"))
like_tweet = str(os.getenv("like_tweet"))
follow_user = str(os.getenv("follow_user"))


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

print("Twitter bot which retweets, like tweets and follow users")
print("Bot Settings")
print("Like Tweets :", like_tweet)
print("Follow users :", follow_user)
print("Keyword searching for :", search_keyword)
print("Sleep time :", sleep_time)

for tweet in tweepy.Cursor(api.search_tweets, q = search_keyword, lang = 'en').items():
	try:
		print('\nTweet by: @' + tweet.user.screen_name)

		tweet.retweet()
		print('Retweeted the tweet')

		# Favorite the tweet
		if like_tweet == "True":
			tweet.favorite()
			print('Favorited the tweet')
		if follow_user == "True":
			if not tweet.user.following:
				tweet.user.follow()
				print('Followed the user')
		
		print("Waiting for ", sleep_time, "seconds")
		sleep(randint (sleep_time , sleep_time+5))
		
			
	except tweepy.errors.Forbidden as e:
		print (e)

	except tweepy.errors.TooManyRequests as f:
		print (f)

	except StopIteration:
		break
#Code by Hem (icecracker_hem on twitter)

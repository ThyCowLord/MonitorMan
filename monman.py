from config import *
import tweepy
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'
session.set('request_token', auth.request_token)
api = tweepy.API(auth)
def main():
  visible_tweets = api.home_timeline()
  for tweet in visible_tweets:
    if tweet == wordsearch:
      tweet_id = tweet.id_str
      status = api.get_status(tweet_id)
      author = status.author
      API.report_spam(author)
      print("Reported and blocked.")
try:
  while True:
    main()
except Exception as error:
  print("Error. The error was: "+error)
  

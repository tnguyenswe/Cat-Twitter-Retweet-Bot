'''
This bot will retweet any twitter page's tweets on their feed in cat language.

It will insert ~meow~ between every single word and also uploads a picture of your choosing. There are multiple
variables that the user needs to change in order to use the program, however.

Consumer Keys and Access Tokens will need to be taken from your own twitter account.
Also, you need to choose the screen name of the user that you want to retweet all the tweets from in cat language.
'''

import random
import tweepy
from tweepy import OAuthHandler

Consumer_API_Key = "XXX"
Consumer_Secret_Key = "XXX"
Access_Token = "XXX"
Access_Token_Secret = "XXX"

auth = tweepy.OAuthHandler(Consumer_API_Key, Consumer_Secret_Key)
auth.set_access_token(Access_Token,Access_Token_Secret)
api = tweepy.API(auth)

def cats(text):
    new = []
    meowText = '~meow~ '
    for i in range(len(text)):
        c = text[i]
        if type(c) == str:
            new.append(c)
        if(c.isspace()) == True:
            new.append(meowText)
    return ''.join(new + [' '] + [meowText])

tweets = api.user_timeline(screen_name ="twitter_username")

for tweet in tweets:
    if tweet.text[0:2] != "RT":
        api.update_with_media('/Users/yourUser/cat_picture.jpg', '@twitter_username {}'.format(cats(tweet.text)), tweet.id)


import praw
import redditscaper
import login

import random
import time
import tweepy

subLists = ['pics', 'mildlyinteresting', 'travel', 'cityporn']


#grab image posts from one of a select group of subreddits and post them on 
#twitter
def postRedditPosts():

    #setup by grabbing posts from reddit
    acc = login.login()
    numPosts = random.randint(5, 15)
    sub = subLists[random.randint(0, len(subLists)-1)]
    posts = redditscaper.getPosts(acc,sub, numPosts)

    #get to twitter
    for submission in posts:
        print('Posting %s' % (submission.title))

if __name__ == "__main__":
    while True: 
        postRedditPosts()

import praw
import time
import os
import re

#Looks for the top posts in a certain subreddit using praw, returns as dict
#Looks for posts with a recognizable image and title.
def getPosts(acc, subreddit, number):
    returnList = []
    subred = acc.subreddit(subreddit)
    numPosts = 0 #Checks how many posts went through
    for submission in subred.hot():

        if numPosts == number: #gathered enough posts
            break
        print(submission.title)

        #filter out inappropriate posts
        if len(submission.selftext) != 0: #cannot be a selftext, must contain media
            continue
        if len(submission.title) + len(submission.url) >= 280: #Want to fit in tweet
            continue
        if submission.permalink[3:7] == 'rpan': #RPAN posts
            continue
        returnList.append(submission)
        time.sleep(1)
        numPosts += 1

    return returnList
    
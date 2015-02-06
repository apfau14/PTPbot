#! /usr/bin/python
# a reddit bot for the PTP subreddit
# BETA

import time
import praw
import random
import re
import logging
import ConfigParser


class PTPbot(object):
    def __init__(self, reddit, conf):
        self.config = conf
        self.reddit = reddit
        self.subreddit = self.reddit.get_subreddit(self.config.get('subreddit', 'subred'))
        self.postTitle = self.config.get('postTitle', 'title')

        login(self.reddit, self.config)      
        logging.info("Login Success")
    # get the desired post
    def get_post(self, post_title):
       return self.subreddit.search(post_title)

    
    def post_flair(user):

    def submit_Post():



def main():
    # establish logging
    logging.basicConfig(filename="PTP.log", level=logging.INFO)
    logging.info("Starting New Logging Session")    
    print "Hello World"
    reddit = praw.Reddit("r/passtheparagraph bot by u/broketheweb and u/AetherGrey")
    # initiate bot here, pass reddit obj and config file location
    config = ConfigParser.ConfigParser()
    # need to do this better than just the file name
    config.read("conf.cnf")
    bot = PTPbot(reddit, config)
    # the inital(weekly) post will always have the same title
    post = bot.get_Post(config.get('postTitle', 'Title');
    logging.info("Post success")

def login(reddit, conf):
    print "Login"
    logging.info(conf.get('account', 'uname'))
    return reddit.login(conf.get('account','uname'), conf.get('account','pwd'))


def count_votes(post):
    # count the votes in the post
	

#compile the winning story from the comments in the post
def compile_story(post):


if __name__ == "__main__":
    main()

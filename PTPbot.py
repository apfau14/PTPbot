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

    def post_flair(self, user):
        pass

    def submit_Post(self):
        pass

    def get_submission(self, submission_id):
        submission = self.reddit.get_submission(submission_id=submission_id)

        return submission

    def compile_winning_story(self, submission):
        '''
        Compile the winning story from the comments in the post into one story
        '''

        winning_comments = submission.comments
        full_story = ''

        # NOTE: Need to iterate down the comment tree, right now it's just
        # printing the first comment

        for comment in winning_comments:
            full_story += comment.body + '\n'

        return full_story


def main():
    # establish logging
    logging.basicConfig(filename="PTP.log", level=logging.INFO)
    logging.info("Starting New Logging Session")
    print("Hello World")
    reddit = praw.Reddit("r/passtheparagraph bot by u/broketheweb and u/AetherGrey")
    # initiate bot here, pass reddit obj and config file location
    config = ConfigParser.ConfigParser()
    # need to do this better than just the file name
    config.read("conf.cnf")
    bot = PTPbot(reddit, config)
    # the inital(weekly) post will always have the same title
    post = bot.get_Post(config.get('postTitle', 'Title'))
    logging.info("Post success")


def login(reddit, conf):
    print("Login")
    logging.info(conf.get('account', 'uname'))
    return reddit.login(conf.get('account', 'uname'), conf.get('account', 'pwd'))


def count_votes(post):
    '''
    Count the votes in the post
    '''
    pass


if __name__ == "__main__":
    main()

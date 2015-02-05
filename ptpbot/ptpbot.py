import praw


class PTPBot(object):
    def __init__(self, reddit):
        self.reddit = reddit

    def run(self):
        '''
        This will be the entry point for the bot.  Everything should run here.
        '''

        # Submission ID is currently just a test, should take in IDs from votes
        submission = self.get_submission('2upwee')
        story = self.get_story_from_winning_submission(submission)

        print(story)

    def get_submission(self, submission_id):
        submission = self.reddit.get_submission(submission_id=submission_id)

        return submission

    def get_story_from_winning_submission(self, submission):
        '''
        Once we have the winning submission, grab all the relevant comments in
        that thread.  Flatten them, and construct them as a string, broken up
        into paragraps.
        '''
        winning_comments = submission.comments

        full_story = ''

        # NOTE: Need to iterate down the comment tree, right now it's just
        # printing the first comment
        for comment in winning_comments:
            full_story += comment.body + '\n'

        return full_story


if __name__ == '__main__':
    main()

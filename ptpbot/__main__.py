from ptpbot import PTPBot
import praw


def main():
    reddit_client = praw.Reddit('A bot for PassTheParagraph')
    bot = PTPBot(reddit_client)

    bot.run()


if __name__ == '__main__':
    main()

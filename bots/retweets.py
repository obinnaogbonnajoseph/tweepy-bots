#!/usr/bin/env python
# tweepy-bots/bots/retweet.py

import tweepy
import logging
from config import create_api
import json
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class RetweetListener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        self.me = api.me()
        self.timeOfRetweet = 0
        self.numberOfTweets = 0

    def on_status(self, tweet):
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                currentTime = time.time()
                timeResult = currentTime - self.timeOfRetweet
                if (timeResult > 900):
                    tweet.retweet()
                    self.timeOfRetweet = time.time()
                    self.numberOfTweets = self.numberOfTweets + 1
                    logger.info(
                        f"***** number of retweets **** {self.numberOfTweets}")
                else:
                    return

            except Exception as e:
                logger.error("Error on retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    api = create_api()
    tweets_listener = RetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])


if __name__ == "__main__":
    main(["#SARSMUSTEND", "#ENDSARSNOW, filter:safe, since:2020-10-12"])

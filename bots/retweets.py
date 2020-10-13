#!/usr/bin/env python
# tweepy-bots/bots/retweet.py

import tweepy
import logging
from config import create_api
import json
import time
# the regular imports, as well as this:
from urllib3.exceptions import ProtocolError
from datetime import datetime

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

        if not tweet.retweeted and not tweet.is_quote_status:
            # Retweet, since we have not retweeted it yet
            try:
                currentTime = time.time()
                timeResult = currentTime - self.timeOfRetweet
                if (timeResult > 300):
                    tweet.retweet()
                    self.timeOfRetweet = time.time()
                    self.numberOfTweets = self.numberOfTweets + 1
                    logger.info(
                        f"***** number of retweets **** {self.numberOfTweets}")
                    logger.info(
                        f"***** current time of retweet {datetime.now()}")
                else:
                    return

            except Exception as e:
                logger.error("Error on retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)
        if status == 327:
            self.timeOfRetweet = 0


def main(keywords):
    api = create_api()
    tweets_listener = RetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    while True:
        try:
            stream.filter(track=keywords, languages=["en"], is_async=True)
        except ProtocolError:
            continue


if __name__ == "__main__":
    main(["#SARSMUSTEND", "#ENDSARSNOW, filter:safe, since:2020-10-12"])

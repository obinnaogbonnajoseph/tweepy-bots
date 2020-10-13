# tweepy-bots
This is a Twitter bot that retweets tweets that meet certain criteria that you put in your code

For example, Retweet all tweets with the hashtag: #EndSars, every 15 mins.


To run your bot on any environment, I assume you must have a developer twitter account.


Here are series of commands to run your bot on any environment

```bash
$ export API_KEY=""
$ export API_SECRET=""
$ export ACCESS_TOKEN=""
$ export ACCESS_TOKEN_SECRET=""

$ source ./venv/bin/activate
$ python bots/retweets.py
```


Please note that you need to do the following:

1. Install python (preferably, python3) on your machine

2. build on a virtual environment. You can easily start working on a virtual environment using this command:
`python3 -m venv venv`

3. install tweepy, preferably on your virtual environment, using this command:
`pip install tweepy`

This repository will undergo lots of changes as time goes, you're welcome to contribute.

#EndSARS

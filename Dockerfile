FROM python:3.7-alpine

COPY bots/config.py /bots/
COPY bots/retweets.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "retweets.py"]
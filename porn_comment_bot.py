from twitter import Twitter, OAuth
from bs4 import BeautifulSoup
from urllib import request
from settings import settings
import random
from __future__ import print_function

t = Twitter(auth=OAuth(settings['OAUTH_TOKEN'],
                       settings['OAUTH_SECRET'],
                       settings['CONSUMER_KEY'],
                       settings['CONSUMER_SECRET'])
            )


def check_comment_length(comment):
    if len(comment) < 140:
        return comment


def get_comment():
    socket = request.Request("http://www.youporn.com/random/video/", headers={'Cookie': 'age_verified=1'})
    a = request.urlopen(socket)
    soup = BeautifulSoup(a)
    comments = soup.find_all("p", {"class": "message"})
    if comments:
        comment = random.choice(comments)
        if check_comment_length(comment.string):
            return comment.string
        else:
            get_comment()


t.statuses.update(status=get_comment())


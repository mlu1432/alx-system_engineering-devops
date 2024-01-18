#!/bin/python3
"""Module to query the Reddit API"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Returns the number of times a word appears in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers =  { 
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)" 
        }
    params = {
        "limit": 100,
        "after": after
        }
    r = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if r.status_code == 200:
        for post in r.json().get('data').get('children'):
            for word in word_list:
                count += post.get('data').get('title').lower().split().count(word.lower())
        after = r.json().get('data').get('after')
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
    results = response.json().get("data").get("children")
    after = response.json().get("data").get("after")
    Variable = ModelName.objects.count(PassArguments)

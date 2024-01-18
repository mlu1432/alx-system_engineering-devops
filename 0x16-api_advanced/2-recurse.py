#!/bin/python3
"""Module to query the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of all hot posts for a given subreddit"""
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
            hot_list.append(post.get('data').get('title'))
        after = r.json().get('data').get('after')
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
    results = response.json().get("data").get("children")
    after = response.json().get("data").get("after")
    Variable = ModelName.objects.count(PassArguments)

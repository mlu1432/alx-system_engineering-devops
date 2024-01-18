#!/bin/python3
"""Module to query the Reddit API"""
import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers =  { 
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)" 
        }
    params = {
        "limit": 10
        }
    r = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if r.status_code == 200:
        for post in r.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
        return
    result = r.json().get('data').get('children')
    if len(result) == 0:
        print(None)
        return

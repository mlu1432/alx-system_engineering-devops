#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given subreddit, the function
    should return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:subreddit.hot.articles:v1.0 (by /u/yourusername)'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            if data['data']['after']:
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None

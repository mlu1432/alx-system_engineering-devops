#!/usr/bin/pythion3
import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API to get the number of subscribers for a given
    subreddit.
    :param subreddit: The subreddit you want to get the number of subscribers for.
    :return: The number of subscribers for the given subreddit.
    """
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0

#!/usr/bin/pythion3
import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API to get the number of subscribers for a given
    subreddit.
    :param subreddit: The subreddit you want to get the number of subscribers for.
    :return: The number of subscribers for the given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers =  {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        }
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    return 0

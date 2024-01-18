#!/usr/bin/python3
"""Module to query the Reddit API"""

import sys
import requests
import json
import time

def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        data = response.json().get("data")
        
        if data:
            children = data.get("children")
            
            if children:
                for post in children:
                    print(post.get("data").get("title"))
            else:
                print("No posts found.")
        else:
            print("Unexpected response format.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
        if response.status_code == 403:
            print("You may be blocked. Check API documentation for more details.")
    except json.decoder.JSONDecodeError as err:
        print(f"Error decoding JSON: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please pass a subreddit name as an argument.")
    else:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)

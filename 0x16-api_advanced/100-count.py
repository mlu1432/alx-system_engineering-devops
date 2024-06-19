#!/usr/bin/python3
"""
100-count.py
"""
import requests

def count_words(subreddit, word_list, hot_list=[], after=None, word_count={}):
    """
    Queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:subreddit.keyword.counter:v1.0 (by /u/yourusername)'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower().split()
            for word in word_list:
                word_lower = word.lower()
                count = title.count(word_lower)
                if count > 0:
                    if word_lower in word_count:
                        word_count[word_lower] += count
                    else:
                        word_count[word_lower] = count

        if data['data']['after']:
            return count_words(subreddit, word_list, hot_list, data['data']['after'], word_count)
        else:
            if word_count:
                sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
                for word, count in sorted_word_count:
                    print(f"{word}: {count}")
            return None
    except requests.RequestException:
        return None

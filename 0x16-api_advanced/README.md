# AXL System Engineering DevOps - API Advanced

This repository contains Python scripts that interact with the Reddit API to perform various tasks.

## Scripts

## 0-subs.py

### 1-top_ten.py

This script queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

**Requirements:**
- Prototype: `def top_ten(subreddit)`
- If not a valid subreddit, print None.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

### 2-recurse.py

This script queries the Reddit API and prints the titles of all hot articles for a given subreddit.

**Requirements:**
- Prototype: `def recurse(subreddit, hot_list=[])`
- If no results are found for the given subreddit, the function should return None.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
- Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function! :)

### 100-count.py

This script queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

**Requirements:**
- Prototype: `def count_words(subreddit, word_list)`
- If word_list contains the same word (case-insensitive), the final count should be the sum of each duplicate.
- Results should be printed in descending order by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically (ascending, from A to Z).
- Words with no matches should be skipped and not printed.
- Words must be printed in lowercase.
- Results are based on the number of times a keyword appears, not titles it appears in.
- Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function! :)

## Usage

To use these scripts, make sure you have Python installed. Then, follow the instructions provided in each script's requirements section.

## Disclaimer

The number presented in the example cannot be accurate now as Reddit's hot articles are always changing.

#!/usr/bin/python3

""" function that queries the Reddit API and prints the titles"""

import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data").get("children")
        for post in data[:10]:
            print(post.get("data").get("title"))
    else:
        print(None)

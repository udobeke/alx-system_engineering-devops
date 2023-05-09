#!/usr/bin/python3

"""a script to count words from a subreddit"""
import requests


def count_words(subreddit, word_list, word_dict={}, after=None):
    """a function to count words from a subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": 'My agent'}
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            title = post['data']['title'].lower().split()

            for word in word_list:
                count = title.count(word.lower())
                if count > 0:
                    if word not in word_dict:
                        word_dict[word] = count
                    else:
                        word_dict[word] += count

        if posts['data']['after'] is not None:
            count_words(subreddit, word_list, word_dict, posts['data']['after'])

        else:
            if len(word_dict) > 0:
                for k, v in sorted(word_dict.items(), key=lambda x: (-x[1], x[0])):
                    print("{}: {}".format(k, v))

            else:
                print()

    else:
        print()

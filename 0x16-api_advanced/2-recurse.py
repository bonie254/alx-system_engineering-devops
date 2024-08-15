#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=""):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])
        after = data.get("after")

        # Append titles to the hot_list
        hot_list.extend(child.get("data", {}).get("title")
                        for child in children)

        # Recursively fetch more posts if "after" is provided
        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list
    except ValueError:
        return None

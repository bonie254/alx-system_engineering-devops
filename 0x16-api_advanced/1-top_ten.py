#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    # Check for a valid response
    if response.status_code != 200:
        print("None")
        return

    try:
        results = response.json().get("data")
        if not results or "children" not in results:
            print("None")
            return

        # Print the titles of the hot posts
        for post in results.get("children", []):
            print(post.get("data", {}).get("title", "None"))

    except ValueError:
        print("None")

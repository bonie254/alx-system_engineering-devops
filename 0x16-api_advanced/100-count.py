#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests
import re


def count_words(subreddit, word_list, instances=None, after=""):
    """Prints counts of given words found in hot posts of a given subreddit."""
    if instances is None:
        instances = {word.lower(): 0 for word in word_list}

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
        return

    try:
        results = response.json().get("data", {})
        children = results.get("children", [])
        after = results.get("after")

        for child in children:
            title = child.get("data", {}).get("title", "").lower()
            words = re.findall(r'\b\w+\b', title)

            for word in word_list:
                word_lower = word.lower()
                count = words.count(word_lower)
                if count > 0:
                    instances[word_lower] += count

        if after:
            count_words(subreddit, word_list, instances, after)
        else:
            sorted_instances = sorted(
                instances.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_instances:
                if count > 0:
                    print(f"{word}: {count}")

    except (ValueError, KeyError):
        return

# Reddit API Scripts

This repository contains Python scripts for interacting with the Reddit API. The scripts demonstrate how to perform tasks such as retrieving subscriber counts, listing hot posts, and analyzing post titles for specific keywords.

## Scripts

### 1. `0-subs.py`

**Description:**  
Queries the Reddit API to return the number of subscribers for a given subreddit.

**Function:**

```python
def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
```

### 2. 1-top_ten.py

**Description:**
Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

**Function:**

```python
    def top_ten(subreddit):
        """Print the titles of the 10 hottest posts on a given subreddit."""
```

### 3. 2-recurse.py

**Description:**
Queries the Reddit API recursively and returns a list of titles of all hot articles for a given subreddit.

**Function:**

```python
    def recurse(subreddit, hot_list=[], after="", count=0):
        """Returns a list of titles of all hot posts on a given subreddit."""
```

**Usage:**
To test the function, add a test call at the end of the script:

```python
    if __name__ == "__main__":
    subreddit = "programming"  # Replace with the subreddit you want to test
    print(recurse(subreddit))

```

### 4. 100-count.py

**Description:**
Queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords. The count is case-insensitive and considers exact matches only.

**Function:**

```python
    def count_words(subreddit, word_list):
        """Prints counts of given words found in hot posts of a given subreddit."""
```

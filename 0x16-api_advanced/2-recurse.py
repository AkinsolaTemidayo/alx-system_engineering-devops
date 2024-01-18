import requests

def recurse(subreddit, hot_list=None, after=None):
    # Base case: If hot_list is None, initialize it as an empty list
    if hot_list is None:
        hot_list = []

    # Reddit API URL for fetching subreddit posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid issues with Too Many Requests
    headers = {'User-Agent': 'Custom-User-Agent'}

    # Add 'after' parameter to the URL if it exists
    if after:
        url += f"?after={after}"

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if there are any posts in the data
        if 'data' in data and 'children' in data['data']:
            # Append titles to the hot_list
            hot_list.extend([post['data']['title'] for post in data['data']['children']])

            # Recursively call the function with the 'after' parameter for pagination
            after = data['data']['after']
            if after:
                recurse(subreddit, hot_list, after)
            else:
                # Base case: Return the hot_list when no more pages are available
                return hot_list
        else:
            # Base case: No posts found in subreddit
            return None
    elif response.status_code == 404:
        # Subreddit not found (invalid subreddit)
        print(f"Subreddit '{subreddit}' not found.")
        return None
    else:
        # Handle other HTTP status codes if needed
        print(f"Error: {response.status_code}")
        return None

# Example usage:
subreddit_name = "python"
hot_articles = recurse(subreddit_name)

if hot_articles:
    print(f"Titles of all hot articles in subreddit '{subreddit_name}':")
    for i, title in enumerate(hot_articles, start=1):
        print(f"{i}. {title}")
else:
    print(f"No results found for subreddit '{subreddit_name}'.")

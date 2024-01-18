import requests

def top_ten(subreddit):
    # Reddit API URL for fetching subreddit posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid issues with Too Many Requests
    headers = {'User-Agent': 'Custom-User-Agent'}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if there are any posts in the data
        if 'data' in data and 'children' in data['data']:
            # Print the titles of the first 10 posts
            for i, post in enumerate(data['data']['children'][:10], start=1):
                print(f"{i}. {post['data']['title']}")
        else:
            print(f"No posts found in subreddit '{subreddit}'.")
    elif response.status_code == 404:
        # Subreddit not found (invalid subreddit)
        print(f"Subreddit '{subreddit}' not found.")
    else:
        # Handle other HTTP status codes if needed
        print(f"Error: {response.status_code}")

# Example usage:
subreddit_name = "python"
top_ten(subreddit_name)

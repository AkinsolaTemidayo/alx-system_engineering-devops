import requests

def number_of_subscribers(subreddit):
    # Reddit API URL for fetching subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid issues with Too Many Requests
    headers = {'User-Agent': 'Custom-User-Agent'}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and return the number of subscribers
        return data['data']['subscribers']
    elif response.status_code == 404:
        # Subreddit not found (invalid subreddit)
        print(f"Subreddit '{subreddit}' not found.")
        return 0
    else:
        # Handle other HTTP status codes if needed
        print(f"Error: {response.status_code}")
        return 0

# Example usage:
subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")

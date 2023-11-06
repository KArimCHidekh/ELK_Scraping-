import requests


class FacebookClient:
    """A class for interacting with the Facebook API."""

    def __init__(self, base_url, access_token):
        """Initialize the Facebook post collector.

        Args:
            access_token: A Facebook access token.
            start_date: The start date to collect posts from.
            end_date: The end date to collect posts to.
        """
        # Create the Facebook Graph API endpoint URL.
        self.base_url = base_url
        self.access_token = access_token

    def get_posts(self, subject, date_range):
        """Get a list of Facebook posts for a given subject.

        Args:
            subject: The subject to get posts for.
            date_range: The start and the end date to collect posts from.
        Returns:
            A list of Facebook posts.
        """

        posts = []
        search_query = f'{subject} since {date_range[0]} until {date_range[1]}'
        params = {
            "q": search_query,
            "access_token": self.access_token,
        }
        print("aaaaaaa: ", self.base_url)
        print("params: ", params)

        params = {
            'fields': 'posts',
            'access_token': self.access_token
        }
        response = requests.get(f"{self.base_url}search", params=params)
        print(response.request)
        print(response.request.url)
        print(response.request.body)

        # Check the response status code.
        if response.status_code == 200:
            data = response.json()
            posts.extend(data["data"])

            # If there is a next page of results, continue fetching results.
            while "paging" in data and "next" in data["paging"]:
                response = requests.get(data["paging"]["next"])
                data = response.json()
                posts.extend(data["data"])
        else:
            raise Exception(f"Failed to collect Facebook posts: {response.status_code}")

        return posts

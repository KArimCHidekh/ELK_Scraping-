import fbmeta


class FacebookClient:
    """A class for interacting with the Instagram API."""

    def __init__(self, access_token, date_range):
        """Initialize the Instagram post collector.

        Args:
            access_token: A Instagram access token.
            start_date: The start date to collect posts from.
            end_date: The end date to collect posts to.
        """

        self.graph = fbmeta.GraphAPI(access_token)
        self.start_date = date_range[0]
        self.end_date = date_range[1]

    def get_posts(self, subject):
        """Get a list of Instagram posts for a given subject.

        Args:
            subject: The subject to get posts for.

        Returns:
            A list of Instagram posts.
        """

        posts = []
        params = {
            "q": subject,
            "type": "post",
            "platform": "instagram",
            "since": self.start_date,
            "until": self.end_date,
        }

        response = self.graph.search(params)
        for post in response["data"]:
            posts.append(post)

        return posts

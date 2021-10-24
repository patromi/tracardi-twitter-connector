import tweepy

from tracardi_twitter_connector.model.model import TwitterCredentials


class TwitterClient:
    def __init__(self, credentials: TwitterCredentials):
        self.credentials = credentials

    async def send(self, message):
        auth = tweepy.OAuthHandler(
            self.credentials.consumer_key,
            self.credentials.consumer_secret
        )
        auth.set_access_token(
            self.credentials.access_token,
            self.credentials.access_token_secret
        )
        api = tweepy.API(auth)
        status = api.update_status(status=message)
        return True

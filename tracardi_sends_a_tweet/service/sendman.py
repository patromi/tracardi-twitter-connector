import tweepy


class SendMan:
    def __init__(self, config):
        self.config = config

    async def send(self, message):
        auth = tweepy.OAuthHandler(
            self.config['consumer_key'],
            self.config['consumer_secret']
        )
        auth.set_access_token(
            self.config['access_token'],
            self.config['access_token_secret']
        )
        api = tweepy.API(auth)
        status = api.update_status(status=message.message)
        return True

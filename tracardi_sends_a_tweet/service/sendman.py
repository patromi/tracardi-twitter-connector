import tweepy


def send(consumer_key, consumer_secret_key):
    try:
        twitter_auth_keys = {
            "consumer_key": consumer_key,
            "consumer_secret": consumer_secret_key,
            "access_token": "1213121841360863232-OLVBdOKrsgCt1JHZnof3k4jkMN9isx",
            "access_token_secret": "VW1NkVZUxddUvDDYrlibBiRFydoScUkMO8RalXBiW8gLF"
        }

        auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
        )

        auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
        )

        api = tweepy.API(auth)

        tweet = """Welcome aboard
                    Please pay attention as we demonstrate
                    The safety features of this aircraft"""

        status = api.update_status(status=tweet)
        return True
    except Exception as e:
        return str(e)

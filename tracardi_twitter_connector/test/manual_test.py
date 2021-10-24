import os

from tracardi.domain.context import Context
from tracardi.domain.entity import Entity
from tracardi.domain.event import Event
from tracardi.domain.profile import Profile
from tracardi.domain.session import Session
from tracardi_plugin_sdk.service.plugin_runner import run_plugin
from tracardi_twitter_connector.plugin import TwitterActions

init = {
    'source': {
        'id': '3dabeb4f-6c0c-4759-b29b-d6c461264ff8'
    },
    # "config": {
    #     "access_token": os.environ['ACCESS_TOKEN'],
    #     "access_token_secret": os.environ['ACCESS_TOKEN_SECRET'],
    #     "consumer_key": os.environ['API_KEY'],
    #     "consumer_secret": os.environ['API_KEY_SECRET']
    # },
    "message": "Testing bot."

}
payload = {}
profile = Profile(id="profile-id")
event = Event(id="event-id",
              type="event-type",
              profile=profile,
              session=Session(id="session-id"),
              source=Entity(id="source-id"),
              context=Context())
result = run_plugin(TwitterActions, init, payload, profile)

print("OUTPUT:", result.output)
print("PROFILE:", result.profile)

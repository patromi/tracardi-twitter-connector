from tracardi.domain.context import Context
from tracardi.domain.entity import Entity
from tracardi.domain.event import Event
from tracardi.domain.profile import Profile
from tracardi.domain.session import Session
from tracardi_plugin_sdk.service.plugin_runner import run_plugin

from tracardi_sends_a_tweet.plugin import TwitterActions

init = {
    'source': {
                'id': '55584df6-9ee3-4acd-a0ea-e555122f3dbc'
                },
    "config": {
        "consumer_key": "",
        "consumer_secret": "",
        "access_token": "",
        "access_token_secret": ""
},
    "message": {"message": "Witam serdecznie"}

}
payload = {}
profile = Profile(id="profile-id")
event = Event(id="event-id",
              type="event-type",
              profile=profile,
              session=Session(id="session-id"),
              source=Entity(id="source-id"),
              context=Context())
result = run_plugin(TwitterActions, init, payload,
                    profile)

print("OUTPUT:", result.output)
print("PROFILE:", result.profile)

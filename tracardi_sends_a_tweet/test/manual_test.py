from tracardi.domain.context import Context
from tracardi.domain.entity import Entity
from tracardi.domain.event import Event
from tracardi.domain.profile import Profile
from tracardi.domain.session import Session
from tracardi_plugin_sdk.service.plugin_runner import run_plugin

from tracardi_sends_a_tweet.plugin import TwitterActions

init = {

        "consumer_key": "Id1IRCPDck8VccPeDDU4L6bT6",

        "consumer_secret_key": "4ITtgk7jDKDiLvBQLuWMHMTtZmh1Xp1lFfRa3BEOoxS9zAqnC5",

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
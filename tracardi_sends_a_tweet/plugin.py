from tracardi_dot_notation.dot_accessor import DotAccessor
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result
from tracardi_sends_a_tweet.model.model import Configuration
from tracardi_sends_a_tweet.service import sendman


class TwitterActions(ActionRunner):

    def __init__(self, **kwargs):
        self.config = Configuration(**kwargs)

    async def run(self, payload):
        dot = DotAccessor(self.profile, self.session, payload, self.event, self.flow)
        consumer_key = dot[self.config.consumer_key]
        consumer_secret_key = dot[self.config.consumer_secret_key]
        send_status = sendman.send(consumer_key, consumer_secret_key)
        if send_status:
            return Result(port="payload", value=payload)
        else:
            return Result(port="payload", value=send_status)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_sends_a_tweet.plugin',
            className='TwitterActions',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Patryk Migaj",
            init={

                "consumer_key": None,

                "consumer_secret_key": None,

            }
        ),
        metadata=MetaData(
            name='tracardi-sends-a-tweet',
            desc='Purpose of this plugin is operations on Twitter account such as send,like,share tweets.',
            type='flowNode',
            width=200,
            height=100,
            icon='icon',
            group=["General"]
        )
    )

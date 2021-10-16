from tracardi_dot_notation.dot_accessor import DotAccessor
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result
from tracardi_sends_a_tweet.model.model import Data, Config, Message
from tracardi_sends_a_tweet.service.sendman import SendMan
from tracardi.service.storage.driver import storage
from tracardi_dot_notation.dot_accessor import DotAccessor
from tracardi.domain.resource import Resource


class TwitterActions(ActionRunner):

    @staticmethod
    async def build(**kwargs) -> 'TwitterActions':
        config = Config(**kwargs)
        data = Data(**kwargs["config"])
        message = Message(**kwargs["message"])
        source = await storage.driver.resource.load(config.source.id)
        source.config = data.dict()
        plugin = TwitterActions(message, source)
        return plugin

    def __init__(self, message: Message, source: Resource):
        self.message = message
        self.sendman = SendMan(source.config)

    async def run(self, payload):
        dot = DotAccessor(self.profile, self.session, payload, self.event, self.flow)
        message = dot[self.message]
        send_status = await self.sendman.send(message)
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

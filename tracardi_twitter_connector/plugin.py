from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result
from tracardi_twitter_connector.model.model import Config, TwitterCredentials
from tracardi_twitter_connector.service.twitter_client import TwitterClient
from tracardi.service.storage.driver import storage
from tracardi_dot_notation.dot_accessor import DotAccessor


class TwitterActions(ActionRunner):

    @staticmethod
    async def build(**kwargs) -> 'TwitterActions':
        config = Config(**kwargs)
        source = await storage.driver.resource.load(config.source.id)
        data = TwitterCredentials(**source.config)

        return TwitterActions(config, data)

    def __init__(self, config: Config, resource_credentials: TwitterCredentials):
        self.config = config
        self.client = TwitterClient(resource_credentials)

    async def run(self, payload):
        dot = DotAccessor(self.profile, self.session, payload, self.event, self.flow)
        message = dot[self.config.message]
        if await self.client.send(message):
            return Result(port="payload", value=payload)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_twitter_connector.plugin',
            className='TwitterActions',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Patryk Migaj",
            init={
                'source': {
                    'id': None
                },
                "message": {
                    "message": "Welcome from bot."
                }
            }),
        metadata=MetaData(
            name='Twitter wall',
            desc='This plugin is tweets to Twitter wall.',
            type='flowNode',
            width=200,
            height=100,
            icon='twitter',
            group=["Connectors"]
        )
    )

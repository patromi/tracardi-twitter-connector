from pydantic import BaseModel


class Configuration(BaseModel):
    consumer_key: str
    consumer_secret_key: str

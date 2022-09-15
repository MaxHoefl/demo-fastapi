from pydantic import BaseSettings, Field


class ServerConfig(BaseSettings):
    LANG: str = Field(default="de")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))

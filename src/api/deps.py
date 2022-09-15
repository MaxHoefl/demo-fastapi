from functools import lru_cache

from fastapi import Depends

from src.api.config import ServerConfig
from src.api.services import JokesService, GermanJokesService, EnglishJokesService
from src.domain.joke import Joke
from loguru import logger


@lru_cache
def acquire_config() -> ServerConfig:
    logger.info("Instantiating ServerConfig")
    return ServerConfig()


def acquire_joke_service(lang: str) -> JokesService:
    if lang == "de":
        logger.info("Instantiating German joke service")
        service = GermanJokesService()
    elif lang == "en":
        logger.info("Instantiating English joke service")
        service = EnglishJokesService()
    else:
        raise ValueError(f"Invalid language: {lang}")
    return service

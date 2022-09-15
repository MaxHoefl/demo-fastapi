
from fastapi import APIRouter, Depends

from src.api.config import ServerConfig
from src.api.deps import acquire_joke_service, acquire_config
from src.api.services import JokesService
from src.domain.joke import Joke
from loguru import logger

jokes_router = APIRouter()


@jokes_router.get("/jokes")
async def get_jokes(
    lang: str,
    joke_service: JokesService = Depends(acquire_joke_service, use_cache=True),
) -> Joke:
    return joke_service.tell_joke()


@jokes_router.post("/jokes")
async def create_joke(
    joke: Joke,
    joke_service: JokesService = Depends(acquire_joke_service, use_cache=True),
) -> Joke:
    return joke_service.store_joke(joke)


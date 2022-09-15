from abc import ABC, abstractmethod
import random
from src.domain.joke import Joke


class JokesService(ABC):
    jokes = [
        Joke(
            title="Witz über Blondine 1",
            content="Was ist eine Blondine mit zwei Gehirnzellen? Schwanger!",
            lang="de"
        ),
        Joke(
            title="Joke about blondes 1",
            content="Why are blonde jokes so short?So they can remember them.",
            lang="en"
        )
    ]

    @abstractmethod
    def tell_joke(self) -> Joke:
        raise NotImplementedError

    def store_joke(self, joke: Joke) -> Joke:
        self.jokes.append(joke)
        return joke


class EnglishJokesService(JokesService):
    def tell_joke(self) -> Joke:
        return random.choice([j for j in self.jokes if j.lang == "en"])


class GermanJokesService(JokesService):
    def tell_joke(self) -> Joke:
        return random.choice([j for j in self.jokes if j.lang == "de"])

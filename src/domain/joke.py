from abc import ABC, ABCMeta, abstractmethod

from pydantic import BaseModel, validator, root_validator, Field

from src.domain.exceptions import JokeValidationException


class JokeValidator(ABC, metaclass=ABCMeta):
    @abstractmethod
    def validate_title(self, title):
        ...


class GermanJokeValidator(JokeValidator):
    def validate_title(self, title):
        if not "Witz" in title:
            raise JokeValidationException(message="German title must contain 'Witz'", model=Joke, error_code="ERR_101")
        return title


class EnglishJokeValidator(JokeValidator):
    def validate_title(self, title):
        if not "Joke" in title:
            raise JokeValidationException(message="English title must contain 'Joke'", model=Joke, error_code="ERR_102")
        return title


class ValidityCheckedModel(BaseModel):
    joke_validator: JokeValidator = Field(default=None, exclude=True)

    class Config:
        arbitrary_types_allowed = True


class Joke(ValidityCheckedModel):
    title: str
    content: str
    lang: str

    class Config:
        post_init_call = "before_validation"

    def __post_init__(self, *args, **kwargs):
        print("__post_init__ is called")
        print(args)
        print(kwargs)

    @root_validator(pre=True)
    def lang_validation(cls, values):
        lang = values["lang"]
        if lang not in ["en", "de"]:
            raise JokeValidationException(message=f"Invalid language: {lang}", model=Joke, error_code="ERR_100")
        val = None
        if lang == "en":
            val = EnglishJokeValidator()
        if lang == "de":
            val = GermanJokeValidator()
        values["joke_validator"] = val
        return values

    @validator("title")
    def title_validation(cls, v, values):
        values["joke_validator"].validate_title(v)
        return v

import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from src.api.routes.jokes import jokes_router
from src.domain.exceptions import JokeValidationException

app = FastAPI(
    title="Jokes App",
    description="You might die laughing",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Max",
        "url": "http://example.com/contact/",
        "email": "max@example.com",
    },
)
app.include_router(jokes_router)


@app.exception_handler(JokeValidationException)
async def unicorn_exception_handler(request: Request, exc: JokeValidationException):
    return JSONResponse(
        status_code=418,
        content={
            "message": exc.message,
            "error_code": exc.error_code,
        },
    )

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    uvicorn.run("src.api.server:app", port=8080, log_level="debug")

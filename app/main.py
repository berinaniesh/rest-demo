from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import user, post, vote, auth
import json, typing
from starlette.responses import Response

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)
app.include_router(auth.router)


class PrettyJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")

@app.get("/", response_class=PrettyJSONResponse)
async def root():
    return {
            "Greeting": "Hello there!",
            "What is this?": "A RESTful backend for a CRUD Application",
            "Authentication": "JWT",
            "Database": "Postgesql",
            "Author": "Berin Aniesh <https://berinaniesh.xyz>",
            "Documentation": "https://rest-demo.berinaniesh.pp.ua/docs",
            "Framework": "FastAPI",
            "Language": "Python",
            "Git Repo": "https://github.com/berinaniesh/rest-demo.git",
            "Contact": "berinaniesh@gmail.com"
            }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import user, post, vote, auth

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


@app.get("/")
async def root():
    return {
            "Greeting": "Hello there!",
            "What is this?": "This is a REST API server which demonstrates a preliminary version of https://api.tncars.pp.ua/docs",
            "Why this?": "I plan to use the original server https://api.tncars.pp.ua for production IRL",
            "Author": "Berin Aniesh <https://berinaniesh.xyz>",
            "Documentation": "https://rest-demo.berinaniesh.pp.ua/docs",
            "Framework": "FastAPI",
            "Language": "Python",
            "Authentication": "JWT",
            "Database": "Postgesql",
            "Git Repo": "https://github.com/berinaniesh/rest-demo.git",
            "Contact": "berinaniesh@gmail.com"
     }

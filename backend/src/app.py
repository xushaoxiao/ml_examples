import io
import os

from fastapi import FastAPI

from .config import settings
from .db import create_db_and_tables, engine


def read(*paths, **kwargs):
    """Read the contents of a text file safety.
    >>> read("project", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        open_file.read()
    return content


description = """
Awesome backend created by me sharing how to build ML engineering.
"""

app = FastAPI(
    title="ml_examples",
    description=description,
    version=read("VERSION"),
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Shaoxiao Xu",
        "url": "http://example.com/contact/",
        "email": "lancexu.hello@gmail.com",
    },
    license_info={
        "name": "The Unlicense",
        "url": "https://unlicense.org",
    },
)

if settings.server and settings.server.get("cors_origins", None):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.server.cors_origins,
        allow_credentials=settings.get("server.cors_allow_credentials", True),
        allow_methods=settings.get("server.cors_allow_methods", ["*"]),
        allow_headers=settings.get("server.cors_allow_headers", ["*"]),
    )


@app.on_event("startup")
def on_startup():
    create_db_and_tables(engine)

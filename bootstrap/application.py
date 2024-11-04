import logging

from fastapi import FastAPI

from app.http.middleware.logging import LoggingMiddleware
from app.http.middleware.trace import TraceMiddleware
from app.providers import app_provider
from app.providers import logging_provider
from app.providers import handle_exception
from app.providers import route_provider
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI(
        title="Aphrodite-py",
        description="API Description",
        version="1.0.0",
        openapi_url="/api-docs/openapi.json",
        docs_url="/swagger-ui/index.html",
        servers=[
              {"url": "http://127.0.0.1:8000",
                  "description": "Development Environmen"},
              {"url": "http://test.aphrodite.com",
                  "description": "Test Environment"},
        ]
    )

    register(app, logging_provider)
    register(app, app_provider)
    register(app, handle_exception)

    boot(app, route_provider)

    app.add_middleware(TraceMiddleware)
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


def register(app, provider):
    provider.register(app)
    logging.info(provider.__name__ + ' registered')


def boot(app, provider):
    provider.boot(app)
    logging.info(provider.__name__ + ' booted')

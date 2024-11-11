from app.providers.database import db, redis_client
from app.settings.config import settings
import logging
import os


def register(app):
    app.debug = settings.DEBUG

    @app.on_event("startup")
    def startup():
        host = os.getenv("APP_SERVER_HOST", "127.0.0.1")
        port = os.getenv("APP_SERVER_PORT", 8000)

        logging.info("===============================")
        logging.info(f"Listening on http://{host}:{port}")
        logging.info(f"Docs addr: http://{host}:{port}/swagger-ui/index.html")
        logging.info("===============================")
        db.connect()

    @app.on_event("shutdown")
    def shutdown():
        if not db.is_closed():
            db.close()

        if redis_client:
            redis_client.close()

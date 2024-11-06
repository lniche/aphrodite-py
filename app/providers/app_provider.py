from app.providers.database import db, redis_client
from settings.config import settings


def register(app):
    app.debug = settings.DEBUG

    # This hook ensures that a connection is opened to handle any queries
    # generated by the request.
    @app.on_event("startup")
    def startup():
        db.connect()

    # This hook ensures that the connection is closed when we've finished
    # processing the request.
    @app.on_event("shutdown")
    def shutdown():
        if not db.is_closed():
            db.close()

        if redis_client:
            redis_client.close()

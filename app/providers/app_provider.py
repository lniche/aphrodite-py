from app.providers.database import db, redis_client
from app.settings.config import settings


def register(app):
    app.debug = settings.DEBUG

    @app.on_event("startup")
    def startup():
        db.connect()

    @app.on_event("shutdown")
    def shutdown():
        if not db.is_closed():
            db.close()

        if redis_client:
            redis_client.close()

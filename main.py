from app.schemas.response import Result
from bootstrap.application import create_app
from config.config import settings
import uvicorn

app = create_app()


@app.get("/", include_in_schema=False)
async def root():
    return "Thank you for using Aphrodite!"


@app.get("/ping",  include_in_schema=False)
async def ping():
    return Result.ok("pong")


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.SERVER_HOST,
                port=settings.SERVER_PORT)

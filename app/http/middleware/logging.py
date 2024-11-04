from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import logging


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if "/api-docs" in request.url.path or "/swagger-ui" in request.url.path or "/docs" in request.url.path or "/redoc" in request.url.path:
            return await call_next(request)

        request_body = await request.body()
        logging.info(f"Request path: {request.url.path}, method: {
                     request.method}, body: {request_body.decode()}")

        response = await call_next(request)

        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk

        logging.info(f"Response status: {response.status_code}, body: {
                     response_body.decode()}")

        return Response(content=response_body, status_code=response.status_code, headers=dict(response.headers))

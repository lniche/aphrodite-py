from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import logging


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if "/api-docs" in request.url.path or "/swagger-ui" in request.url.path or "/docs" in request.url.path or "/redoc" in request.url.path:
            return await call_next(request)

        content_type = request.headers.get('Content-Type', '')
        if 'application/json' not in content_type:
            return await call_next(request)

        trace_id = getattr(request.state, 'trace_id', None)
        if trace_id is None:
            logging.warning(
                "Request ID is not available in LoggingMiddleware.")

        request_body = await request.body()
        logging.info(f"Request path: {request.url.path}, method: {
                     request.method}, body: {request_body.decode()},trace_id: {trace_id}")

        async def receive():
            return {
                "type": "http.request",
                "body": request_body,
                "more_body": False
            }
        request._receive = receive
        response = await call_next(request)

        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk

        logging.info(f"Response status: {response.status_code}, body: {
                     response_body.decode()},trace_id: {trace_id}")

        return Response(content=response_body, status_code=response.status_code, headers=dict(response.headers))

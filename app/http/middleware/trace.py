from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import uuid


class TraceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("x-request-id")

        if not request_id:
            request_id = str(uuid.uuid4())

        request.state.request_id = request_id

        response = await call_next(request)

        response.headers["x-request-id"] = request_id

        return response

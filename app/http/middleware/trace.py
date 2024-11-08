from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import uuid


class TraceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        trace_id = request.headers.get("X-Request-ID")

        if not trace_id:
            trace_id = str(uuid.uuid4())

        request.state.trace_id = trace_id
        response = await call_next(request)

        response.headers["X-Request-ID"] = trace_id

        return response

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from app.logger.logger import logger
import time
import json

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Log request info
        logger.info(f"Request: {request.method} {request.url} | Headers: {dict(request.headers)}")

        try:
            response: Response = await call_next(request)
        except Exception as exc:
            logger.exception(f"Unhandled Exception for {request.method} {request.url}: {exc}")
            raise exc

        process_time = time.time() - start_time
        content_length = response.headers.get("content-length", "0")

        logger.info(
            f"Response: {request.method} {request.url} | Status: {response.status_code} | "
            f"Time: {process_time:.3f}s | Content-Length: {content_length}"
        )
        return response

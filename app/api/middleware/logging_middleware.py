from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.background import BackgroundTask
from app.domain.services.loggingService import log_db_upload
import logging

logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, dispatch = None):
        super().__init__(app, dispatch)

    async def dispatch(self, request: Request, call_next):
        try:
            request_data = {
                "method": request.method,
                "path": request.url.path,
                "headers": dict(request.headers),
                "body": (await request.body()).decode("utf-8"),
            }

            response = await call_next(request)

            chunks = []
            async for chunk in response.body_iterator:
                chunks.append(chunk)
            res_body = b"".join(chunks)

            response_data = {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "body": res_body.decode("utf-8"),
            }

            task = BackgroundTask(
                log_db_upload,
                request_data,
                response_data
            )

            return Response(
                content=res_body,
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.media_type,
                background=task,
            )
        except Exception as e:
            logger.error(f"There was a problem uploading the request: {e}")
            raise e

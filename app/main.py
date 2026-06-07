from api_exception import register_exception_handlers
from app.core.lifespan import lifespan
from starlette.requests import Request
from uuid import uuid4
from app.core.logger import log
from fastapi import FastAPI
from app.api.v1.routers import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
)
register_exception_handlers(app)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid4())
    request_logger = log.bind(request_id=request_id)
    request_logger.info("Request received", method=request.method, url=str(request.url))
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    request_logger.info("Response sent", status_code=response.status_code)
    return response


app.include_router(api_router, prefix=settings.API_V1_STR)

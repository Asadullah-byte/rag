from api_exception import BaseExceptionCode


class CustomExceptionCode(BaseExceptionCode):
    LIFESPAN_INIT_ERROR = (
        "LITE-500",
        "Lifespan initialization failed",
        "Lifespan initialization failed",
    )
    NAME_REQUIRED = (
        "NR-422",
        "Name query parameter is required",
        "Name query parameter is required",
    )
    SIMULATED_ERROR = (
        "SE-500",
        "This is a simulated error for testing purposes",
        "Simulated error occurred for testing",
    )

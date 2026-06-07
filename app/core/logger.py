from structlog.processors import CallsiteParameter
import logging
import structlog

logging.basicConfig(level=logging.DEBUG)


def format_callsite(
    _, __, event_dict
):  # formating the callsite information to a single string for readability
    func_name = event_dict.pop("func_name", "?")
    lineno = event_dict.pop("lineno", "?")
    pathname = event_dict.pop("pathname", "?")
    event_dict["location"] = f"{pathname}|{func_name}:{lineno}"
    return event_dict


structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.add_log_level,
        structlog.processors.CallsiteParameterAdder(
            {
                CallsiteParameter.FUNC_NAME,
                CallsiteParameter.LINENO,
                CallsiteParameter.PATHNAME,
            }
        ),
        format_callsite,
        structlog.dev.ConsoleRenderer(),
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)
log = structlog.get_logger()

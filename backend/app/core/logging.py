import logging
import sys

LOG_FORMAT = (
    "level=%(levelname)s "
    "logger=%(name)s "
    "message=%(message)s "
)

def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        stream=sys.stdout,
        force=True,
    )
import logging


module_logger = logging.getLogger(__name__)


def do_something() -> None:
    print("DO_SOMETHING_START")

    # using module_logger instead of directly logging
    module_logger.info("GREETINGS_FROM_DO_SOMETHING")

    print("DO_SOMETHING_END")

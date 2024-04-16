# Logging Means - Capturing details which are useful for debugging
# and show the execution details of program to  user
# Warning to the users
# information to the users
# errors, critical errors to users

import logging

def test_print_logs():
    Logger = logging.getLogger(__name__)
    # Intentional logs to the users
    Logger.info("This is information logs")
    Logger.warning("This is a warning logs")
    Logger.error("This is an error log")
    Logger.critical("This is a critical error log")

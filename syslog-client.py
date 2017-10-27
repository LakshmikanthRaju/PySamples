#!/usr/bin/env python

import argparse
import logging
import logging.handlers

parser = argparse.ArgumentParser(__file__,
                                 description="A syslog message generator")

parser.add_argument("--address", "-a",
                    default="localhost",
                    help="The syslog message recipient address")

parser.add_argument("--port", "-p",
                    type=int, default=514,
                    help="The syslog message recipient port")

parser.add_argument("--level", "-l",
                    default="DEBUG",
                    help="The syslog message log level")

parser.add_argument("--message", "-m",
                    required=True,
                    help="The syslog message")


def string_to_level(log_level):
    """ Convert a commandline string to a proper log level
    @param string log_level     command line log level argument
    @return logging.LEVEL       the logging.LEVEL object to return
    """
    if log_level == "CRITICAL":
        return logging.CRITICAL
    if log_level == "ERROR":
        return logging.ERROR
    if log_level == "WARNING":
        return logging.WARNING
    if log_level == "INFO":
        return logging.INFO
    if log_level == "DEBUG":
        return logging.DEBUG
    return logging.NOTSET


if __name__ == "__main__":
    args = parser.parse_args()
    #print args

    log = logging.getLogger('SyslogLogger') #logging.getLogger(__name__)
    log.setLevel(string_to_level(args.level))

    handler = logging.handlers.SysLogHandler(address=(args.address, args.port), facility=19)
    formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.addHandler(logging.FileHandler('pylogger.log'))

    log.log(logging.WARNING, args.message)
    log.debug("this is debug message")
    log.warning("this is warning message")
    log.error("this is error message")
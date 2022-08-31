#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 16:48
# @Author  : Arrow
# @Describe:

import logging
import os

from logging.handlers import RotatingFileHandler


def get_logger(app_name, file_path, log_level):
    """Generate a standard logger
      Args:
        name - logger object
        file_path - the log file path
        log_level - log level, defalt value is INFO
    """
    # Create the directory if it does not exist
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as msg:
            raise Exception("Can't make directory %s. %s" % (directory, msg))

    file_handler = RotatingFileHandler(file_path, maxBytes=10 * 1024 * 1024,
                                       backupCount=5, encoding="UTF-8")
    fmt = "%(asctime)s [%(levelname)s] %(threadName)s %(filename)s:%(lineno)d - %(message)s"
    formatter = logging.Formatter(fmt)
    file_handler.setFormatter(formatter)
    _logger = logging.getLogger(app_name)
    _logger.addHandler(file_handler)
    _logger.setLevel(log_level)

    class ContextualFilter(logging.Filter):
        def filter(self, log_record):
            # no logger for logview thread
            if log_record.threadName.startswith('logview'):
                return False
            return True

    _logger.addFilter(ContextualFilter())
    return _logger
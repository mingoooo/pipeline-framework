import logging
import os

fm = logging.Formatter('%(asctime)s [%(levelname)s] (%(module)s): %(message)s')


def get_logger(name=None, level='info', log_path=None):
    logger = logging.getLogger(name)
    s_handler = logging.StreamHandler()
    s_handler.setFormatter(fm)
    s_handler.setLevel(logging.DEBUG)
    logger.addHandler(s_handler)
    if log_path is not None:
        _set_log_file(logger, log_path)
    _set_log_level(logger, level)
    return logger


def _set_log_level(logger, level):
    logger.setLevel(getattr(logging, level.upper()))


def _set_log_file(logger, log_path):
    if not os.path.isfile(log_path):
        fd = open(log_path, 'w')
        fd.close()
    handler = logging.FileHandler(log_path)
    handler.setFormatter(fm)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

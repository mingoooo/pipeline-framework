import importlib
from util.log import get_logger
from config import config

logger = get_logger(
    name='handle',
    level=config.get('log', {}).get('log_level', 'info'),
    log_path=config.get('log', {}).get('log_path'))


def load_handle(name, *args, **kwargs):
    module = importlib.import_module('handles.' + name)
    cs = getattr(module, 'Handle')
    return cs(*args, **kwargs)


class HandleError(Exception):
    pass


class BaseHandle(object):
    def run(self):
        raise NotImplementedError

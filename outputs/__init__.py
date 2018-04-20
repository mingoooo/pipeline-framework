import importlib
from util.log import get_logger
from config import config

logger = get_logger(
    name='output',
    level=config.get('log', {}).get('log_level', 'info'),
    log_path=config.get('log', {}).get('log_path'))


def load_output(name, *args, **kwargs):
    module = importlib.import_module('outputs.' + name)
    cs = getattr(module, 'Output')
    return cs(*args, **kwargs)


class OutputError(Exception):
    pass


class BaseOutput(object):
    def run(self):
        raise NotImplementedError

import importlib
from util.log import get_logger
from config import config

logger = get_logger(
    name='input',
    level=config.get('log', {}).get('log_level', 'info'),
    log_path=config.get('log', {}).get('log_path'))


def load_input(name, *args, **kwargs):
    module = importlib.import_module('inputs.' + name)
    cs = getattr(module, 'Input')
    return cs(*args, **kwargs)


class InputError(Exception):
    pass


class BaseInput(object):
    def run(self):
        raise NotImplementedError

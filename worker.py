import time
from util.log import get_logger
from config import config


logger = get_logger(
    name='worker',
    level=config.get('log', {}).get('log_level', 'info'),
    log_path=config.get('log', {}).get('log_path'))


class WorkerError(Exception):
    pass


class Worker(object):
    def __init__(self, input_, handle, output, interval=.2):
        self.input = input_
        self.handle = handle
        self.output = output
        self.interval = interval
        logger.debug('Create worker')

    def start(self):
        logger.debug('Start worker')
        while True:
            input_result = self.input.run()
            logger.debug('Input result: %s' % input_result)

            handle_result = self.handle.run(input_result)
            logger.debug('Handle result: %s' % handle_result)

            output_result = self.output.run(input_result)
            logger.debug('Output result: %s' % output_result)

            time.sleep(self.interval)

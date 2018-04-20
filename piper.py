from multiprocessing import Process
from inputs import load_input
from handles import load_handle
from outputs import load_output
from worker import Worker
from config import config
import time


def _create_worker_process(input_, handle, output, interval=.2):
    worker = Worker(input_, handle, output, interval)
    return Process(target=worker.start, daemon=True)


def _start_piper(*worker_confs):
    worker_pool = [
        _create_worker_process(
            load_input(conf['input']['name'], **conf['input'].get('kwargs', {})),
            load_handle(conf['handle']['name'], **conf['handle'].get('kwargs', {})),
            load_output(conf['output']['name'], **conf['output'].get('kwargs', {})))
        for conf in worker_confs
    ]

    for w in worker_pool:
        w.start()
    return worker_pool


def main():
    """
    Start pipeline worker daemon
    """

    worker_confs = config.get('workers', [])
    assert worker_confs, 'Worker config not found'
    is_alive = False
    worker_pool = []

    while True:
        if not is_alive:
            for p in worker_pool:
                p.terminate()
            worker_pool = _start_piper(*worker_confs)
            is_alive = True

        for p in worker_pool:
            if not p.is_alive():
                is_alive = False
                break

        time.sleep(.1)


if __name__ == '__main__':
    main()

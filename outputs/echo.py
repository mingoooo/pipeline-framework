from outputs import BaseOutput


class Output(BaseOutput):
    def __init__(self, prefix=''):
        self.prefix = prefix

    def run(self, msg):
        return self.prefix + msg

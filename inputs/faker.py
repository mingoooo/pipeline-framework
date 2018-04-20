from faker import Faker
from inputs import BaseInput


class Input(BaseInput):
    def __init__(self):
        self.fake = Faker()

    def run(self):
        return self.fake.name()

import yaml
import os


conf_path = os.path.join(os.path.dirname(__file__), 'config.yml')

with open(conf_path, 'rb') as fd:
    config = yaml.load(fd)

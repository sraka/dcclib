import os
import logging
import json
import sys
from pprint import pprint
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
# sys.path.append("/home/akash/_data/repos/arlo/src/python/acg/lib/py2")
import utils.pJson


config_file = os.path.join(os.path.dirname(__file__), "config.json")
# config_data = utils.pJson.read_json(config_file)
config_data = utils.pJson.read_json(config_file)
pprint(config_data)
# with open(config_file, 'r') as f:
#     config_data = f.read()
# config_data = json.loads(config_data)

class Logger(object):
    def __init__(self):
        pass

    def presets(self):
        pass

#
# print type(config_data)
# print config_data.get("presets").get("divider")
# print type(config_data.get("presets").get("divider"))
# exec (config_data.get("presets").get("newline"))
# exec(config_data.get("presets").get("divider"))


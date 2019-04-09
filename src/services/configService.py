import json
import os

class ConfigService:

    @staticmethod
    def __get_config(environment):
        with open(os.path.dirname(os.path.abspath(__file__ + '../../../')) + '/config/env/env.json') as json_data:
            return json.load(json_data).get(environment)

    def __init__(self,environment):
        self.environment = environment
        config =self.__get_config(environment)
        self.config = config


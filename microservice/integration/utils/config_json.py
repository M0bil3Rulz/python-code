import json
from json import JSONDecodeError


class ConfigJson(object):
    """
    Class to manage integration testing options
    """
    __configuration = {}

    def __init__(self, config_file):
        self.__configuration = self.parse_file(config_file)

    def get_settings(self):
        """
        Return a copy of the settings that were loaded

        :return:
        """
        return self.__configuration

    def parse_file(self, config_file):
        """
        Opens a text file that is in json form and loads it into local variable for later use

        :param config_file: json format settings file
        :return:
        """
        try:
            with open(config_file, "r") as json_file:
                json_contents = json.load(json_file)
        except JSONDecodeError as ex:
            raise Exception("Invalid Json File", ex)

        return json_contents

    def get_log_path(self):
        """
        Note: defaulting to specified location if user did not put a value in json configuration file
        :return:
        """
        return self.__configuration.get('log_filename', None)

    def get_log_level(self):
        """
        Note: defaulting to specified logging level if user did not put a value in json configuration file
        :return:
        """
        return self.__configuration.get('log_level', 'info')

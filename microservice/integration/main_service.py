import logging
import logging.handlers
import os
import sys

import integration.utils.custom_logger as logger

from integration.utils.command_line import CommandLine
from integration.utils.config_json import ConfigJson


def integration_testing():
    """
    Run main services
    """
    try:
        main_execution = MainService()
        main_execution.run()
        sys.exit(0)
    except Exception as ex:
        print(ex)
        sys.exit(1)


class MainService(CommandLine, object):
    """
    Main class for launching end to end tests
    """
    __config = {}

    def __init__(self, *args, **kwargs):
        super(MainService, self).__init__(*args, **kwargs)
        self.log = logging.getLogger()
        args = self.parse_args()
        self.__config = ConfigJson(args.config_json)

        logger.set_log_level(self.__config.get_log_level())
        logger.set_log_file_path(self.__config.get_log_path())
        logger.add_standard_out()
        
        self.log.info("Command line: %s", args)
        self.log.info("Python folder: %s", os.path.dirname(sys.executable))
        self.log.info("Current working directory: {}".format(os.getcwd()))

    def run(self):
        self.log.info("Running integration tests")
        sys.exit(0)

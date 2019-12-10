import argparse
import scripts


class CommandLine(argparse.ArgumentParser, object):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("description", "Python application to run integration tests")
        argparse.ArgumentParser.__init__(self, *args, **kwargs)

        self.add_argument(
            "--config_json",
            dest="config_json",
            help="Specify JSON configuration file for the integration tests.",
            required=True)
        self.add_argument(
            "--log_level",
            dest="log_level",
            default="info",
            type=str.upper,
            help="Logging level - debug, info, warn, error, or critical.")
        self.add_argument(
            "--stdout",
            action="store_true",
            help="Print output to stdout")
        self.add_argument(
            "--version",
            action="version",
            version="%(prog)s {version}".format(version=scripts.__version__)
        )

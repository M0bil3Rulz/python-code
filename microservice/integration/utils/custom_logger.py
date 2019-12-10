import coloredlogs
import logging
import logging.handlers
import os
import sys

from distutils.dir_util import mkpath

level_styles = {
    'debug': {
        'color': 'magenta'
    },
    'info': {
        'color': 'white'
    },
    'warn': {
        'color': 'yellow'
    },
    'error': {
        'color': 'red',
        'bold': True,
    },
    'critical': {
        'background': 'red',
        'bold': True,
    },
}

log = logging.getLogger(__name__[:-len('.log')])

formatter = logging.Formatter(fmt='%(asctime)s %(filename)s %(levelname)-8s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
formatter_colored = coloredlogs.ColoredFormatter(fmt='%(asctime)s %(filename)s %(levelname)-8s %(message)s',
                                                 datefmt='%Y-%m-%d %H:%M:%S', level_styles=level_styles)
handler = None
handler_console = None

log_level = logging.INFO

_log_levels = {'DEBUG': logging.DEBUG,
               'INFO': logging.INFO,
               'WARN': logging.WARN,
               'ERROR': logging.ERROR,
               'CRITICAL': logging.CRITICAL}


def set_log_file_path(path):
    global handler, handler_console, log, formatter, formatter_colored
    try:
        if path != 'stdout':
            mkpath(os.path.dirname(path))
            handler = logging.FileHandler(path, encoding='utf-8')
            handler.setFormatter(formatter)
            logging.getLogger().addHandler(handler)
            logging.getLogger().setLevel(log_level)
        else:
            handler_console = logging.StreamHandler(sys.stdout)
            handler_console.setFormatter(formatter)
            coloredlogs.install(logger=log, level=log_level, isatty=True)
            logging.getLogger().addHandler(handler_console)
            logging.getLogger().setLevel(log_level)
    except Exception as ex:
        log.addHandler(logging.StreamHandler(sys.stdout))
        raise Exception("Unable to create log file: {}".format(ex))


def add_standard_out():
    global handler, handler_console, log, formatter, formatter_colored
    handler_console = logging.StreamHandler(sys.stdout)
    handler_console.setFormatter(formatter)
    coloredlogs.install(logger=log, level=log_level, isatty=True)
    logging.getLogger().addHandler(handler_console)
    logging.getLogger().setLevel(log_level)


def set_log_level(level):
    global _log_levels, log_level, log
    if level in _log_levels:
        log.setLevel(_log_levels[level])
        log_level = _log_levels[level]
    else:
        log.setLevel(logging.INFO)


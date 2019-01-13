import abc

import kontroll.command

from kontroll import logger
from kontroll import util

import six


LOG = logger.get_logger(__name__)


@six.add_metaclass(abc.ABCMeta)
class Base(object):
    "Abstract base class defining command interface"

    def __init__(self, config):
        self._config = config
        self._setup()
    
    @abc.abstractmethod
    def execute(self):
        pass
    
    def print_info(self):
        msg = "Region: '{}'".format(self._config.active_region.name)
        LOG.info(msg)
        msg = "Action: '{}'".format(util.underscore(self.__class__.__name__))
        LOG.info(msg)

    def _setup(self):
        pass
        #self._config.provisioner.write_config()
        #self._config.provisioner.manage_inventory()


def execute_subcommand(config, subcommand):
    command_module = getattr(kontroll.command, subcommand)
    command = getattr(command_module, util.camelize(subcommand))

    return command(config).execute()

def _get_subcommand(string):
    return string.split('.')[-1]
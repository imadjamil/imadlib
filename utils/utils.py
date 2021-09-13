import logging


logger = logging.getLogger("utils-logger")


class Utils:
    def __init__(self):
        pass

    def _logger(self):
        if logger:
            return logger
        else:
            raise Exception("logger is empty")

    def _test(self):
        self._logger.info("This is test")
        # raise NotImplementedError

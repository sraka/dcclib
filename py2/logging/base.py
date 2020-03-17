import logging

class Logger(object):

    def __init__(self, class_name):
        super(Logger, self).__init__()
        self.__logger = logging.getLogger(class_name)
        self.set_handler("stream")
        self.build()

    @property
    def logger(self):
        return self.__logger

    def build(self):
        """
        build the logger instance.
        if user wants to set different handler user need to call this function after doing so.
        :return:
        """
        self.__formatter = logging.Formatter('%(asctime)s %(message)s')
        self.__handler.setFormatter(self.__formatter)
        self.__logger.addHandler(self.__handler)

    def set_handler(self, handler):
        """
        setter for log handler.
        :param handler:
        :return:
        """
        if handler == "file":
            self.__handler = logging.FileHandler()
        elif handler == "stream":
            self.__handler = logging.StreamHandler()


"""
USE:
        from tau.logging.base import Logger
        
        self._logger = Logger(__name__).logger
        self._logger.info(error)
        
Currenlty being used:
        logger = Logger(__name__).logger
        logging.basicConfig(level=logging.INFO)
        log_line_separator = "-" * 79
        
manual method of using
        import logging
        
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("[%(lineno)s] %(levelname)s:" " %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False
        
        logger.info("export dir = {}".format(export_paths))
"""
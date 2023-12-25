import logging
import json


class Logger:

    def __init__(self, log_file_name='agent.log', log_level=logging.ERROR):
        self.log_file_name = log_file_name
        self.log_level = log_level
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.log_level)
        file_handler = logging.FileHandler(self.log_file_name)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log(self, message, data, log_level=logging.INFO):
        try:
            message = self.message_format(message, data)
            if log_level == logging.DEBUG:
                self.logger.debug(message)
            elif log_level == logging.INFO:
                self.logger.info(message)
            elif log_level == logging.WARNING:
                self.logger.warning(message)
            elif log_level == logging.ERROR:
                self.logger.error(message)
            elif log_level == logging.CRITICAL:
                self.logger.critical(message)
        except Exception as e:
            print('Error in log')
            print(e)

    def message_format(self, message_string, data={}):
        try:
            message_string += ' '
            if (isinstance(data, list) or isinstance(data, dict)
                    or isinstance(data, tuple)) and len(data) > 0:
                message_string += json.dumps(data)
            elif isinstance(data, str):
                message_string += data
            elif isinstance(data, int) or isinstance(data, float) or isinstance(
                    data, bool):
                message_string += str(data)
            elif data is None:
                message_string += 'None'
            else:
                message_string += str(data)
        except Exception as e:
            message_string += str(e)
        return message_string

    def info(self, message, data={}):
        self.log(message, data, logging.INFO)

    def debug(self, message, data={}):
        self.log(message, data, logging.DEBUG)

    def warning(self, message, data={}):
        self.log(message, data, logging.WARNING)

    def error(self, message, data={}):
        self.log(message, data, logging.ERROR)

    def critical(self, message, data={}):
        self.log(message, data, logging.CRITICAL)

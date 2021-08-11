import logging


def setup_logger(logger_name, log_file, level=logging.DEBUG):
    my_log = logging.getLogger(logger_name)
    formatter = logging.Formatter('[ %(asctime)s ] [ %(levelname)-4s ] %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    my_log.setLevel(level)
    my_log.addHandler(fileHandler)
    my_log.addHandler(streamHandler)


setup_logger('controller_log', r'log/controller_log.log')
controller_log = logging.getLogger('controller_log')
setup_logger('service_log', r'log/service_log.log')
service_log = logging.getLogger('service_log')
setup_logger('dao_log', r'log/dao_log.log')
dao_log = logging.getLogger('dao_log')

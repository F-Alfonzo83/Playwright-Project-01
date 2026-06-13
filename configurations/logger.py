import logging


def _logger(name):

    #Set Logger Level
    logger = logging.getLogger(name)

    #Create Handler
    stream_handler = logging.StreamHandler()

    #Set Logging level for Streamer
    stream_handler.setLevel(logging.DEBUG)

    #Formater
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    #Set Formatter
    stream_handler.setFormatter(formatter)

    #Set Logger Handler
    logger.addHandler(stream_handler)

    return logger

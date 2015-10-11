import logging

formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

def set_stream_handler(logger):
    logger.handlers = []
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)

def set_file_handler(logger, path):
    logger.handlers = []
    hdlr = logging.FileHandler(path)
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)

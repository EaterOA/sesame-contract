import argparse
import asyncio
import logging

import sesamecontract.util.logging as logutil

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class SesameServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.peer = transport.get_extra_info("peername")
        logger.debug("Received connection from {}:{}".format(self.peer[0], self.peer[1]))

    def data_received(self, data):
        self.transport.write(data)

    def connection_lost(self, exc):
        logger.debug("Lost connection to {}:{}".format(self.peer[0], self.peer[1]))

def parse_args():
    parser = argparse.ArgumentParser()
    return parser.parse_args()

def main():
    logutil.set_stream_handler(logger)
    args = parse_args()
    loop = asyncio.get_event_loop()
    server = loop.create_server(SesameServerProtocol, port=4499)
    loop.run_until_complete(server)
    logger.debug("Starting server")
    loop.run_forever()

if __name__ == '__main__':
    main()

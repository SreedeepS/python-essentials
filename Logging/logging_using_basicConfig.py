import sys
import logging

#The logging stack comes with a utility function, basicConfig, which can be used to perform some basic configurations

logging.basicConfig(
    level="INFO",
    format="%(levelname)s: %(message)s",
    stream=sys.stdout
)
logging.info("Hello world!")
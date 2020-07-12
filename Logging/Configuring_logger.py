import logging
import sys

#Get a handle of the root logger by calling getLogger without any arguments
root_logger = logging.getLogger()

#Create a stream handler, which will output to sys.stdout (the console)
handler = logging.StreamHandler(sys.stdout)

#Create a formatter to configure how we want the logs to look.
formatter = logging.Formatter("%(levelname)s: %(message)s")

#Bind them together by setting the formatter in the handler and the handler in the logger
handler.setFormatter(formatter)
root_logger.addHandler(handler)

#Set the level in the logger
root_logger.setLevel("INFO")

logging.info("Hello logging world")
import logging
from  logging.config import fileConfig
fileConfig("log_config.ini")
logging.info("Log using configuration file")
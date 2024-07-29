import logging


'''
Never ignore an exception that transmits an error silently.
Never raise and log an error
'''

logger = logging.getLogger("logger_name")

#By default, the logging stack will be configured to log warning, error and fatal
logger.debug("Logging at debug")
logger.info("Logging at info")
logger.warning("Logging at warning")
logger.error("Logging at error")
logger.fatal("Logging at fatal")
print('----------------'*5)
#when you log, you should pass some variable or information that helps us with the current state of the application
system = "mars module"
for number in range(3):
    logger.warning("%d errors reported in %s", number, system)

print('----------------'*5)

#To include the exception and trace back the full information, you can use the exc_info argument

try:
    int("nope")
except Exception:
    logging.error("Something bad happened", exc_info=True)
print('----------------'*5)

#Call the 'exception' method to achieve the same as using error with exc_info:
try:
    int("nope")
except Exception:
    logging.exception("Something bad happened")

print('----------------'*5)

#Example output difference of exc_info versus logging an exception string
#We should not be capturing broad exceptions and formatting them manually as part of a log message.

d = dict()
# Prefer
try:
    d["missing_key"] += 1
except Exception:
    logging.error("Something bad happened", exc_info=True)

#The output in the below approach will only print the text of the exception, without further information.
#We don't know if it was a key error, nor where the issue appeared. 

print('----------------'*5)
# to
try:
    d["missing_key"] += 1
except Exception as e:
    logging.error("Something bad happened: %s", e)
#******************************
#
# NAME      : lwlogger.py
# AUthOR    : Chris Anderson
# EMAIL     : chris.anderson@andersonleatherworks.com
9# DATE      : 08/18/2021
# PURPOSE   : This file contains all the logging modules
#
#******************************

# Imports
import logging as alwlog
from datetime import datetime as date

class alwlogging:
# Globals
    global __alwLogName
    global __spaces1
    global __spaces2

    # Beging Logging
    def log_begin(name, log):
        global __alwLogName
        global __spaces1
        global __spaces2
        # create logger
        __spaces1 = ' ' * 25
        __spaces2 = ' ' * 12
        today = date.today()
        dt_string = '%Y%m%d'
        curDate = today.strftime('%s'%(dt_string))
        __alwLogName = '%s%s.log'%(log, curDate)
        alwlog.basicConfig(filename=__alwLogName, filemode='a', format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = alwlog.getLogger(__alwLogName)
        logger.setLevel(alwlog.DEBUG)

        logger.info('**********************************************')
        logger.info('*')
        logger.info('*  Starting %s'%(name))

    # End Logging
    def log_end(name):
        alwlog.basicConfig(filename=__alwLogName, filemode='a', format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = alwlog.getLogger(__alwLogName)
        logger.setLevel(alwlog.DEBUG)

        logger.info('*')
        logger.info('*  Ending %s'%(name))
        logger.info('*')
        logger.info('**********************************************')

    # Debug
    def debug(name ,s):
        logger = alwlog.getLogger(__alwLogName)
        alwlog.basicConfig(filename=__alwLogName, filemode='a', format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger.setLevel(alwlog.DEBUG)
        logger.debug('*')
        logger.debug( '*    DEBUG : %s:\n%s*%s%s'%(name, __spaces1, __spaces2, s))

    # Info
    def info(name ,s):
        logger = alwlog.getLogger(__alwLogName)
        alwlog.basicConfig(filename=__alwLogName, filemode='a', format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger.setLevel(alwlog.DEBUG)
        logger.info('*')
        logger.info( '*    INFO : %s:\n%s*%s%s'%(name, __spaces1, __spaces2, s))

    # Warning
    def warn(name ,s):
        logger = alwlog.getLogger(__alwLogName)
        alwlog.basicConfig(filename=__alwLogName, filemode='a', format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger.setLevel(alwlog.DEBUG)
        logger.warning('*----------------------------------')
        logger.warning( '*    WARNING : %s:\n%s*%s%s'%(name, __spaces1, __spaces2, s))
        logger.warning('*----------------------------------')

    # Critical
    def crit(name ,s):
        logger = alwlog.getLogger(__alwLogName)
        alwlog.basicConfig(filename=__alwLogName, filemode='a', format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger.setLevel(alwlog.DEBUG)
        logger.critical('*++++++++++++++++++++++++++++++++++')
        logger.critical( '*    CRITICAL : %s:\n%s*%s%s'%(name, __spaces1, __spaces2, s))
        logger.critical('*++++++++++++++++++++++++++++++++++')

# Main Logging Section            
if __name__ == '__main__':
   print ('This is the lwlogger.py file' )  
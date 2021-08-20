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
import logging as lwlog
from datetime import date
from common_package.common_modules import common
class lwlogging:
# Globals
    global lwLogName
    # Beging Logging

    def __init__(self):
        global lwLogName

    def log_begin(name, log):
        global lwLogName
        print("log_begin")
        # create logger
        dt_string = common.get_currDate('%m/%d/%Y')
        tm_string = common.get_currtime('%H:%M:%S')
        lwLogName = log
        
        lwlog.basicConfig(filename=lwLogName, filemode='a', format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = lwlog.getLogger('lwcosting')
        logger.setLevel(lwlog.DEBUG)

        logger.info('**********************************************')
        logger.info('*')
        logger.info('*  Starting %s'%(name))

    # End Logging
    def log_end(name):
        print("log_end")
        today = date.today()
        dt_string = today.strftime("%m/%d/%Y %H:%M:%S")
        lwlog.basicConfig(filename=lwLogName, filemode='a', format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = lwlog.getLogger('lwcosting')
        logger.setLevel(lwlog.DEBUG)

        logger.info('*')
        logger.info('*  Ending %s'%(name))
        logger.info('*')
        logger.info('**********************************************')

    # Debug
    def debug(name ,s):
        logger = lwlog.getLogger('lwcosting')
        lwlog.basicConfig(filename=lwLogName, filemode='a', format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger.setLevel(lwlog.DEBUG)
        logger.debug('*')
        logger.debug( '*    DEBUG : %s: %s'%(name,s))

    # Info
    def info(name ,s):
        logger = lwlog.getLogger('lwcosting')
        lwlog.basicConfig(filename=lwLogName, filemode='a', format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger.setLevel(lwlog.DEBUG)
        logger.info('*')
        logger.info( '*    INFO : %s: %s'%(name,s))

    # Warning
    def warn(name ,s):
        logger = lwlog.getLogger('lwcosting')
        lwlog.basicConfig(filename=lwLogName, filemode='a', format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger.setLevel(lwlog.DEBUG)
        logger.warning('*----------------------------------')
        logger.warning( '*    WARNING : %s: %s'%(name,s))
        logger.warning('*----------------------------------')

    # Critical
    def crit(name ,s):
        logger = lwlog.getLogger('lwcosting')
        lwlog.basicConfig(filename=lwLogName, filemode='a', format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger.setLevel(lwlog.DEBUG)
        logger.critical('*++++++++++++++++++++++++++++++++++')
        logger.critical( '*    CRITICAL : %s: %s'%(name,s))
        logger.critical('*++++++++++++++++++++++++++++++++++')

# Main Logging Section            
if __name__ == '__main__':
   print ('This is the lwlogger.py file' )  
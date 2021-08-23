#******************************
#
# NAME      : common_module.py
# AUthOR    : Chris Anderson
# EMAIL     : chris.anderson@andersonleatherworks.com
# DATE      : 08/18/2021
# PURPOSE   : This file contains all the common modules
#
#******************************
from datetime import datetime as date
from common_package.alwlogger import alwlogging as alwlog
import ctypes
import glob
import os
from sys import exec_prefix

class common:
   global module
   module = 'common_module'

   def deleteAllButCurrent(currLogFileName, fPath, fExt):
      func = 'deleteAllButCurrent'
      file_path = fPath+currLogFileName+fExt

      alwlog.info('%s.%s'%(module,func), 'Preparing to delete all files except %s'%(currLogFileName))
      if os.path.isfile(file_path):
         # get list of files that match
         alwlog.info('%s.%s'%(module,func), 'Getting a list of all files in %s, \n with the extention of %s'%(fPath, fExt))
         cleanupFiles = glob.glob(fPath + '*' +fExt)
         alwlog.info('%s.%s'%(module,func), 'Removing %s from list'%(file_path))
         cleanupFiles.remove(file_path)
         for cleanupFile in cleanupFiles:
            alwlog.info('%s.%s'%(module,func), 'Deleting File %s' %cleanupFile)
            os.remove(cleanupFile)
         alwlog.info('%s.%s'%(module,func), 'Deleting Files Completed')
      else:
         alwlog.crit('%s.%s'%(module,func), '**Cannot find file in path %s'%( file_path))
         

   def fileclose(fo):
      fo.close()

   def fileOpen(fileToOpen):
      func='fileOpen'
      try:
         fo = open(os.path.join(fileToOpen))
         return fo
      except (FileNotFoundError):
         alwlog.crit('%s.%s'%(module,func),'**File ("%s") was not found...**'%(fileToOpen))
         return
      return result   

   def get_currDate(dateFormat):
      func = 'get_currDate'
      alwlog.info('%s.%s'%(module,func), 'Getting Current Date using Date Format %s'%(dateFormat))
      today = date.today()
      curDate = today.strftime('%s'%(dateFormat))
      alwlog.info('%s.%s'%(module,func), 'Returning %s as current date'%(curDate))
      return curDate

   def get_currtime(timeFormat):
      func = 'get_currDate'
      alwlog.info('%s.%s'%(module,func), 'Getting Current Time using Time Format %s'%(timeFormat))
      now = date.now()
      
      curTime = now.strftime('%s'%(timeFormat))
      return curTime

   def get_logName(logfileName, fileDateFormat):
      func = 'get_logName'
      file_date = common.get_currDate('%s'%(fileDateFormat))
      LogfileName = '%s-%s.log'%(logfileName, file_date)
      return LogfileName

   def make_emptyFile(fn):
      # Write file.
      open(fn, 'a').close()

      # For windows set file attribute.
      if os.name == 'nt':
         ret = ctypes.windll.kernel32.SetFileAttributesW(file_name,
                                                         FILE_ATTRIBUTE_HIDDEN)
         if not ret: # There was an error.
            raise ctypes.WinError()


if __name__ == '__main__':
   print ('This is the common.py file' )  
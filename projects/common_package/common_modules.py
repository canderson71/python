#******************************
#
# NAME      : common_module.py
# AUthOR    : Chris Anderson
# EMAIL     : chris.anderson@andersonleatherworks.com
# DATE      : 08/18/2021
# PURPOSE   : This file contains all the Common modules
#
#******************************
from datetime import datetime as date
from common_package.alwlogger import ALWLogging as alwlog
import ctypes
import glob
import os
from sys import exec_prefix

class Common:
   global __module
   __module = 'common_module'

   def _deleteAllButCurrent(currLogFileName, fPath, fExt):
      func = 'deleteAllButCurrent'
      file_path = fPath+currLogFileName+fExt

      alwlog._info('%s.%s'%(__module,func), 'Preparing to delete all files except %s'%(currLogFileName))
      if os.path.isfile(file_path):
         # get list of files that match
         alwlog._info('%s.%s'%(__module,func), 'Getting a list of all files in %s, \n with the extention of %s'%(fPath, fExt))
         cleanupFiles = glob.glob(fPath + '*' +fExt)
         alwlog._info('%s.%s'%(__module,func), 'Removing %s from list'%(file_path))
         cleanupFiles.remove(file_path)
         for cleanupFile in cleanupFiles:
            alwlog._info('%s.%s'%(__module,func), 'Deleting File %s' %cleanupFile)
            os.remove(cleanupFile)
         alwlog._info('%s.%s'%(__module,func), 'Deleting Files Completed')
      else:
         alwlog._crit('%s.%s'%(__module,func), '**Cannot find file in path %s'%( file_path))
         
   def _fileclose(fo):
      fo.close()

   def _fileOpen(fileToOpen):
      func='fileOpen'
      try:
         fo = open(os.path.join(fileToOpen))
         return fo
      except (FileNotFoundError):
         alwlog._crit('%s.%s'%(__module,func),'**File ("%s") was not found...**'%(fileToOpen))
         return
      return result   

   def _getcurrDate(dateFormat):
      func = 'get_currDate'
      alwlog._info('%s.%s'%(__module,func), 'Getting Current Date using Date Format %s'%(dateFormat))
      today = date.today()
      curDate = today.strftime('%s'%(dateFormat))
      alwlog._info('%s.%s'%(__module,func), 'Returning %s as current date'%(curDate))
      return curDate

   def _getcurrtime(timeFormat):
      func = '_getcurrtime'
      alwlog._info('%s.%s'%(__module,func), 'Getting Current Time using Time Format %s'%(timeFormat))
      now = date.now()
      
      curTime = now.strftime('%s'%(timeFormat))
      return curTime

   def _getlogName(logfileName, fileDateFormat):
      func = '_getlogName'
      file_date = Common.get_currDate('%s'%(fileDateFormat))
      LogfileName = '%s-%s.log'%(logfileName, file_date)
      return LogfileName

   def _make_emptyFile(fn):
      # Write file.
      open(fn, 'a').close()

      # For windows set file attribute.
      if os.name == 'nt':
         ret = ctypes.windll.kernel32.SetFileAttributesW(file_name,
                                                         FILE_ATTRIBUTE_HIDDEN)
         if not ret: # There was an error.
            raise ctypes.WinError()


if __name__ == '__main__':
   print ('This is the Common.py file' )  
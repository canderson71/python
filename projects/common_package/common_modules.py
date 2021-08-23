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
import os
import ctypes

class common:
   global module
   module = 'common_module'

   def fileclose(fo):
      fo.close()

   def fileOpen(fileToOpen):
      fo = open(os.path.join(fileToOpen))
      return fo

   def get_currDate(dateFormat):
      func = 'get_currDate'
      today = date.today()
      curDate = today.strftime('%s'%(dateFormat))
      print (curDate)
      return curDate

   def get_currtime(timeFormat):
      func = 'get_currDate'
      now = date.now()
      
      curTime = now.strftime('%s'%(timeFormat))
      print (curTime)
      return curTime

   def get_logName(logfileName, fileDateFormat):
      print('1 Log File Name : %s'%(logfileName))
      func = 'get_logName'
      file_date = common.get_currDate('%s'%(fileDateFormat))
      LogfileName = '%s-%s.log'%(logfileName, file_date)
      print('2 Log File Name : %s'%(LogfileName))
      return LogfileName

   def is_hidden(filepath):
    name = os.path.basename(os.path.abspath(filepath))
    return name.startswith('.') or common.has_hidden_attribute(filepath)

   def has_hidden_attribute(filepath): 
      try:
         attrs = ctypes.windll.kernel32.GetFileAttributesW(unicode(filepath))
         assert attrs != -1
         result = bool(attrs & 2)
      except (AttributeError, AssertionError):
         result = False
      return result   

   def make_emptyFile(fn):
      # Write file.
      open(fn, 'a').close()

      # For windows set file attribute.
      if os.name == 'nt':
         ret = ctypes.windll.kernel32.SetFileAttributesW(file_name,
                                                         FILE_ATTRIBUTE_HIDDEN)
         if not ret: # There was an error.
            raise ctypes.WinError()

   def make_hiddenFile(fn):
      FILE_ATTRIBUTE_HIDDEN = 0x02
      # Write file.
      with open(fn, 'w') as f:
         pass

      # For windows set file attribute.
      if os.name == 'nt':
         ret = ctypes.windll.kernel32.SetFileAttributesW(file_name,
                                                         FILE_ATTRIBUTE_HIDDEN)
         if not ret: # There was an error.
            raise ctypes.WinError()

if __name__ == '__main__':
   print ('This is the common.py file' )  
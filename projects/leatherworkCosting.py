#******************************
#
# NAME      : leatherworkCosting.py
# AUthOR    : Chris Anderson
# EMAIL     : chris.anderson@andersonleatherworks.com
# DATE      : 08/18/2021
# PURPOSE   : This is the main LeatherWorkCosting 
#
# -----------------------------
#  Coding Style
#   __name      : Global variable
#   _name       : self written function name
#   CapWords    : Class Names
#
#******************************

# Imports
from logging import log
from common_package.common_modules import Common as c
from common_package.db_common import DBCommon as db
from common_package.alwlogger import ALWLogging as alwlog
from common_package.tk_common import TKCommon as lwtk
from datetime import datetime as date
from db_tables import dbtables as tables
from modal_form import app as mf
from pathlib import Path as p
from tkinter import *
from tkinter import messagebox as msgbx

import os
import sys
import tkinter as tk

global __dbName
global __logFileName
global __version

class Costing(tk.Tk):
    # Initilization
    def __init__(self):
        global __appTitle
        global __dbName
        global __logFileName
        global __module
        global __version

        __appTitle = 'Leather Work Costing'
        __dbName = 'LeatherWorks'
        __module = 'leatherworkCosting'
        __version = 'v0.10'
        __logFileName = 'logging/lw-Costing-log-'

        alwlog._logbegin('Leather Work Costing',__logFileName)

        lwtk._tkinit(self)
        self.protocol('WM_DELETE_WINDOW', Costing.on_closing())
        #frame = tk.Frame(self).pack(side=TOP)

        if not os.path.exists('logging'):
            os.mkdir('logging')
        #mf.InputBox(frame)

        Costing._create_menubar(self)
        self.text = tk.Text()
        self.text.pack(side='top', fill='both', expand=True)

        #create buttons on bottom
        #bottomBtn = lwtk._tkbtn(frame, "Quit", "on_quit",)

    # Create TK Menu
    def _create_menubar(self):
        # create a menu for the menubar and associate it
        # with the window
        func = '_create_member'
        alwlog._info('%s.%s'%(__module,func),'Creating Menu Bar')
        #self.protocol('WM_DELETE_WINDOW', Costing.on_closing())

        # Set screen size and center it
        window_height = 500
        window_width = 1200
        lwtk._tkgeoemtry(self, window_height, window_width)

        # Set the title and __version in the title
        menubar = lwtk._tktitle(self, __appTitle, __version)

        # create a File menu and add it to the menubar
        file_menu = lwtk._tkcreateTopMenu(self, menubar, 'File')
        file_menu.add_command(label='Quit', underline=2, command=self.on_quit)

        # create a Edit menu and add it to the menubar
        edit_menu = lwtk._tkcreateTopMenu(self, menubar, 'Edit')
        edit_menu.add_command(label='Clear', underline=2, command=self.on_clear)

        # create a database menu and add it to the menubar
        _dbmenu = lwtk._tkcreateTopMenu(self, menubar, 'Database')
        _dbmenu.add_command(label='List Tables', underline=2, command=self.on_list)
        _dbmenu.add_command(label='ReCreate DB', underline=2, command=self.on_recreate)
        _dbmenu.add_command(label='Delete Database', underline=2, command=self.on_delete)

        # create a Log menu and add it to the menubar
        log_menu = lwtk._tkcreateTopMenu(self, menubar, 'Logs')
        log_menu.add_command(label='View Current Log', underline=2, command=self.on_log)
        log_menu.add_command(label='Delete Older Logs', underline=2, command=self.on_deleteLog)

        alwlog._info('%s.%s'%(__module,func),'Menu Bar Created')

    # Log stuff to TEXT in Program
    def _log(self, s):
        func = 'log'
        alwlog._info('%s.%s'%(__module,func),'Logging to TEXT area')
        try:
            self.text.insert('end', s + '\n')
            self.text.see('end')
            self.text.pack()
        except Exception as err:
            alwlog._crit('%(module)s.%(func)s', '***%(err)s')

    # Edit Menu
    def on_clear(self): 
        func = 'on_clear'
        alwlog._info('%s.%s'%(__module,func),'Clearing TEXT area')
        confirmtxt = 'Are you sure you want to clear the form'
        level = 'info'
        try:
            if lwtk._tkmsgbxAskOkCancel(confirmtxt, level):
                alwlog._info('%s.%s'%(__module,func),'TEXT Area Cleared')
                self.text.delete('1.0','end')
            else:
                alwlog._info('%s.%s'%(__module,func),'Clacelled Clearing TEXT Area')
        except Exception as err:
            alwlog._crit('%(module)s.%(func)s', '***%(err)s')

    # Exit program via close button
    def on_closing():
        func = 'on_closing'
        alwlog._info('%s.%s'%(__module,func), "on_quit was called")

        confirmtxt = 'Are you sure you want to quit?'
        level = 'info'
        try:
            if lwtk._tkmsgbxAskOkCancel(confirmtxt, level):
                alwlog.log_end('%s.%s'%(__module,func))
                sys.exit(0)
            else:
                alwlog._info('%s.%s'%(__module,func), "on_quit cancelled")
        except Exception as err:
            alwlog._crit('%(module)s.%(func)s', '***%(err)s')

    # Delete Database
    def on_delete(self):
        func = 'on_delete'
        alwlog._warn('%s.%s'%(__module,func),'Deleting databases')

        confirmtxt = 'This will delete the database.\nThis is irreversable.\n\nAre you sure?'
        level = 'warning'
        try:
            if lwtk._tkmsgbxAskOkCancel(confirmtxt, level):
                mydb = db._dbopenConnection('root', '1961@PJAnd3r50n')
                db._dbdeleteDB(mydb.cursor(), __dbName)
                db._dbcloseConnection(mydb)

                alwlog._info('%s.%s'%(__module,func),'   Deletion Successful')
                return True
            else:
                alwlog._info('%s.%s'%(__module,func),'  DB Deletion Canceled')
                return False
        except Exception as err:
            alwlog._crit('%s.%s'%(__module,func), '***%s'%(str(err)))

    def on_deleteLog(self):
        func = 'on_deleteLog'
        alwlog._info('%s.%s'%(__module,func), 'Deleting All Logs older than today')
        confirmtxt = 'Are you sure you want to delete all older logs?'
        level = 'warning'
        if lwtk._tkmsgbxAskOkCancel(confirmtxt, level):
            try:
                curDate = c._getcurrDate('%Y%m%d')
                logFile = __logFileName+curDate
                print(logFile)
                alwlog._info('%s.%s'%(__module,func), 'Deleting ALL Files *EXCEPT* %s'%(logFile))
                newLogFile = logFile.replace('logging/','')
                c._deleteAllButCurrent(newLogFile, './logging/', '.log')
            except Exception as err:
                alwlog._crit('%s.%s'%(__module,func), '***%s'%(err))
    # List DB tables
    def on_list(self):
        global __dbName
        func = 'on_list'
        alwlog._info('%s.%s'%(__module,func),'Listing DB Tables')

        __dbName = 'LeatherWorks'
        dbUser = 'leatherworker'
        dbUserPWD = '1960@And3r50n'

        mydb = db._dbopenConnection(dbUser, dbUserPWD)
        dbtableList = db._dbtablelist(mydb.cursor(), __dbName)
        self._log('Database : ' + __dbName)
        try:
            for table in dbtableList:
                self._log('  ' + ''.join(table))
            db._dbcloseConnection(mydb)  
        except Exception as err:
            alwlog._crit('%(module)s.%(func)s', '***%(err)s')

    def on_log(self): 
        func = 'on_log'
        alwlog._info('%s.%s'%(__module,func),'View Current Log')
        alwlog._info('%s.%s'%(__module,func),'Clearing current TEXT area')
        self.text.delete('1.0','end')
        curDate = c._getcurrDate('%Y%m%d')
        newLogFile = __logFileName.replace('logging/','')
        newlogfileName = newLogFile+curDate+'.log'
        try:    
            if not os.path.isfile(newlogfileName):
                alwlog._info('%s.%s'%(__module,func),'    opening log file for reading')
                fo = c._fileOpen('./logging/'+newlogfileName)
                line = fo.read()
                Costing._log(self, line)
                # Close opend file
                c._fileclose(fo)
            else:
                alwlog._crit('%s.%s'%(__module,func),'    Log File (%s) does not exist '%(newlogfileName))
        except Exception as err:
            alwlog._crit('%s.%s'%(__module,func), '***%s'%(err))

    # Exit program
    def on_quit(self): 
        func = 'on_quit'
        alwlog._info('%s.%s'%(__module,func), "on_quit was called")
        confirmtxt = 'Are you sure you want to quit?'
        level = 'warning'
        if lwtk._tkmsgbxAskOkCancel(confirmtxt, level):
            alwlog._logend('%s.%s'%(__module,func))
            sys.exit(0)
        else:
            alwlog._info('%s.%s'%(__module,func), "on_quit cancelled")

    # Delete DB Tables and Database, and recreate them
    def on_recreate(self):
        func = 'on_recreate'
        alwlog._warn('%s.%s'%(__module,func),'Recreate Database and Tables')
    
        confirmtxt = 'This will destroy all current data, delete and recreate the database.\nThis is unreversable.\n\nAre you sure?'
        level = 'warning'
        try:
            if lwtk._tkmsgbxAskOkCancel(confirmtxt, level):
                alwlog._info('%s.%s'%(__module,func),'  Destroying and Recreating databases')
                mydb = db._dbopenConnection('root', '1961@PJAnd3r50n')

                __dbName = 'LeatherWorks'
                dbUser = 'leatherworker'
                dbUserPWD = '1960@And3r50n'

                db._dbdeleteDB(mydb.cursor(), __dbName)
                db._dbcreateDB(mydb, __dbName)
                db._dbcreateTables(mydb.cursor(), tables._make_tables())
                db._dbgrantUserPriv(mydb.cursor(), __dbName, dbUser)
                db._dbcloseConnection(mydb)

                alwlog._info('%s.%s'%(__module,func),'  Destroying and Recreating databases Complete')
                return True
            else:
                alwlog._info('%s.%s'%(__module,func),'  Recreated Cancelled')
                return False
        except Exception as err:
            alwlog._crit('%(module)s.%(func)s', '***%(err)s')

#Main App loop
if __name__ == '__main__':
    fn = p('python3.sys')

    if not fn.is_file():
        c._make_emptyFile(fn)
        #Run Initialization

    app = Costing()
    app.mainloop()

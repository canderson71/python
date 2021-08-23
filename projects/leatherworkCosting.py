#******************************
#
# NAME      : leatherworkCosting.py
# AUthOR    : Chris Anderson
# EMAIL     : chris.anderson@andersonleatherworks.com
# DATE      : 08/18/2021
# PURPOSE   : This is the main LeatherWorkCosting 
#
#******************************

# Imports
from logging import log
from common_package.common_modules import common as c
from common_package.db_common import dbcommon as db
from common_package.alwlogger import alwlogging as alwlog
from common_package.tk_common import tkcommon as lwtk
from datetime import datetime as date
from db_tables import dbtables as tables
from modal_form import app as mf
from pathlib import Path as p
from tkinter import *
from tkinter import messagebox as msgbx

import os
import sys
import tkinter as tk

global Version
global dbName
global logFileName

class costing(tk.Tk):
    # Initilization
    def __init__(self):
        global Version
        global module
        global dbName
        global appTitle
        global logFileName

        appTitle = 'Leather Work Costing'
        dbName = 'LeatherWorks'
        module = 'leatherworkCosting'
        Version = 'v0.10'
        lwtk.tk_init(self)
        
        if not os.path.exists('logging'):
            os.mkdir('logging')
        #mf.InputBox(self)

        self._create_menubar()
        self.text = tk.Text()
        self.text.pack(side='top', fill='both', expand=True)

    # Create TK Menu
    def _create_menubar(self):
        # create a menu for the menubar and associate it
        # with the window
        func = '_create_member'
        alwlog.info('%s.%s'%(module,func),'Creating Menu Bar')
        self.protocol('WM_DELETE_WINDOW', self.on_closing)

        # Set screen size and center it
        window_height = 500
        window_width = 1200
        lwtk.tk_geoemtry(self, window_height, window_width)

        # Set the title and version in the title
        menubar = lwtk.tk_title(self, appTitle, Version)

        # create a File menu and add it to the menubar
        file_menu = lwtk.tk_createTopMenu(self, menubar, 'File')
        file_menu.add_command(label='Quit', underline=2, command=self.on_quit)

        # create a Edit menu and add it to the menubar
        edit_menu = lwtk.tk_createTopMenu(self, menubar, 'Edit')
        edit_menu.add_command(label='Clear', underline=2, command=self.on_clear)

        # create a database menu and add it to the menubar
        db_menu = lwtk.tk_createTopMenu(self, menubar, 'Database')
        db_menu.add_command(label='List Tables', underline=2, command=self.on_list)
        db_menu.add_command(label='ReCreate DB', underline=2, command=self.on_recreate)
        db_menu.add_command(label='Delete Database', underline=2, command=self.on_delete)

        # create a Log menu and add it to the menubar
        log_menu = lwtk.tk_createTopMenu(self, menubar, 'Logs')
        log_menu.add_command(label='View Current Log', underline=2, command=self.on_log)
        log_menu.add_command(label='Delete Older Logs', underline=2, command=self.on_deleteLog)

        alwlog.info('%s.%s'%(module,func),'Menu Bar Created')

    # Log stuff to TEXT in Program
    def log(self, s):
        func = 'log'
        alwlog.info('%s.%s'%(module,func),'Logging to TEXT area')
        self.text.insert('end', s + '\n')
        self.text.see('end')
        self.text.pack()

    # Edit Menu
    def on_clear(self): 
        func = 'on_clear'
        alwlog.info('%s.%s'%(module,func),'Clearing TEXT area')
        confirmtxt = 'Are you sure you want to clear the form'
        level = 'info'
        if lwtk.tk_msgbxAskOkCancel(confirmtxt, level):
            alwlog.info('%s.%s'%(module,func),'TEXT Area Cleared')
            self.text.delete('1.0','end')
        else:
            alwlog.info('%s.%s'%(module,func),'Clacelled Clearing TEXT Area')

   # Exit program via close button
    def on_closing(self):
        func = 'on_closing'
        alwlog.info('%s.%s'%(module,func), "on_quit was called")

        confirmtxt = 'Are you sure you want to quit?'
        level = 'info'
        if lwtk.tk_msgbxAskOkCancel(confirmtxt, level):
            alwlog.log_end('%s.%s'%(module,func))
            sys.exit(0)
        else:
            alwlog.info('%s.%s'%(module,func), "on_quit cancelled")

    # Delete Database
    def on_delete(self):
        func = 'on_delete'
        alwlog.warn('%s.%s'%(module,func),'Deleting databases')

        confirmtxt = 'This will delete the database.\nThis is irreversable.\n\nAre you sure?'
        level = 'warning'
        if lwtk.tk_msgbxAskOkCancel(confirmtxt, level):
            mydb = db.db_openConnection('root', '1961@PJAnd3r50n')
            db.db_deleteDB(mydb.cursor(), dbName)
            db.db_closeConnection(mydb)

            alwlog.info('%s.%s'%(module,func),'   Deletion Successful')
            return True
        else:
            alwlog.info('%s.%s'%(module,func),'  DB Deletion Canceled')
            return False

    def on_deleteLog(self):
        func = 'on_deleteLog'
        alwlog.info('%s.%s'%(module,func), 'Deleting All Logs older than today')
        confirmtxt = 'Are you sure you want to delete all older logs?'
        level = 'warning'
        if lwtk.tk_msgbxAskOkCancel(confirmtxt, level):
            curDate = c.get_currDate('%Y%m%d')
            logFile = logFileName+curDate
            alwlog.info('%s.%s'%(module,func), 'Deleting ALL Files *EXCEPT* %s'%(logFile))
            newLogFile = logFile.replace('logging/','')
            c.deleteAllButCurrent(newLogFile, './logging/', '.log')
    
    # List DB tables
    def on_list(self):
        global dbName
        func = 'on_list'
        alwlog.info('%s.%s'%(module,func),'Listing DB Tables')

        dbName = 'LeatherWorks'
        dbUser = 'leatherworker'
        dbUserPWD = '1960@And3r50n'

        mydb = db.db_openConnection(dbUser, dbUserPWD)
        dbtableList = db.db_tablelist(mydb.cursor(), dbName)
        self.log('Database : ' + dbName)
        for table in dbtableList:
            self.log('  ' + ''.join(table))
        db.db_closeConnection(mydb)  

    def on_log(self): 
        func = 'on_log'
        alwlog.info('%s.%s'%(module,func),'View Current Log')
        alwlog.info('%s.%s'%(module,func),'    Clearing current TEXT area')
        self.text.delete('1.0','end')
        curDate = c.get_currDate('%Y%m%d')
        newLogFile = logFileName.replace('logging/','')
        newlogfileName = newLogFile+curDate+'.log'
        if not os.path.isfile(newlogfileName):
            alwlog.info('%s.%s'%(module,func),'    opening log file for reading')
            try:
                fo = c.fileOpen('./logging/'+newlogfileName)
                line = fo.read()
                costing.log(self, line)
                # Close opend file
                c.fileclose(fo)
            except Exception as err:
                alwlog.crit('%s.%s'%(module,func),'    EXCEPTION HAS OCCURRED\nstr(%s)'%(err))
        else:
            alwlog.crit('%s.%s'%(module,func),'    Log File (%s) does not exist '%(newlogfileName))

    # Exit program
    def on_quit(self): 
        func = 'on_quit'
        alwlog.info('%s.%s'%(module,func), "on_quit was called")
        confirmtxt = 'Are you sure you want to quit?'
        level = 'warning'
        if lwtk.tk_msgbxAskOkCancel(confirmtxt, level):
            alwlog.log_end('%s.%s'%(module,func))
            sys.exit(0)
        else:
            alwlog.info('%s.%s'%(module,func), "on_quit cancelled")

    # Delete DB Tables and Database, and recreate them
    def on_recreate(self):
        func = 'on_recreate'
        alwlog.warn('%s.%s'%(module,func),'Recreate Database and Tables')
    
        confirmtxt = 'This will destroy all current data, delete and recreate the database.\nThis is unreversable.\n\nAre you sure?'
        level = 'warning'
        if lwtk.tk_msgbxAskOkCancel(confirmtxt, level):
            alwlog.info('%s.%s'%(module,func),'  Destroying and Recreating databases')
            mydb = db.db_openConnection('root', '1961@PJAnd3r50n')

            dbName = 'LeatherWorks'
            dbUser = 'leatherworker'
            dbUserPWD = '1960@And3r50n'

            db.db_deleteDB(mydb.cursor(), dbName)
            db.db_createDB(mydb, dbName)
            db.db_createTables(mydb.cursor(), tables._make_tables())
            db.db_grantUserPriv(mydb.cursor(), dbName, dbUser)
            db.db_closeConnection(mydb)

            alwlog.info('%s.%s'%(module,func),'  Destroying and Recreating databases Complete')
            return True
        else:
            alwlog.info('%s.%s'%(module,func),'  Recreated Cancelled')
            return False

#Main App loop
if __name__ == '__main__':
    logFileName = 'logging/lw-costing-log-'
    alwlog.log_begin('Leather Work Costing',logFileName)

    fn = p('python3.sys')

    if not fn.is_file():
        c.make_emptyFile(fn)
        #Run Initialization

    app = costing()
    app.mainloop()

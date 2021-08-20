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
from common_package.db_common import dbcommon as db
from tkinter import *
from tkinter import messagebox as msgbx
from common_package.lwlogger import lwlogging as lwlog
import tkinter as tk
import sys
import os

global Version

class costing(tk.Tk):
    # Initilization
    def __init__(self):
        global Version
        global module
        module = "leatherworkCosting"
        Version = "0.10"
        tk.Tk.__init__(self)
        
        self._create_menubar()
        self.text = tk.Text()
        self.text.pack(side="top", fill="both", expand=True)

    # Create TK Menu
    def _create_menubar(self):
        # create a menu for the menubar and associate it
        # with the window
        func = "_create_member"
        lwlog.info("%s.%s"%(module,func),"Creating Menu Bar")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Disable screen resizing
        self.resizable(False, False)  # This code helps to disable windows from resizing

        # Set screen size and center it
        window_height = 500
        window_width = 1200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # Set the title and version in the title
        self.title("Leather Work Costing         v.%s"%(Version))
        self.menubar = tk.Menu()
        self.configure(menu=self.menubar)

        # create a File menu and add it to the menubar
        file_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Quit", command=self.on_quit)

        # create a Edit menu and add it to the menubar
        edit_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Clear", underline=2, command=self.on_clear)

        # create a database menu and add it to the menubar
        db_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Database", menu=db_menu)
        db_menu.add_command(label="List Tables", underline=2, command=self.on_list)
        db_menu.add_command(label="ReCreate DB", underline=2, command=self.on_recreate)
        db_menu.add_command(label="Delete Database", underline=2, command=self.on_delete)

        # create a View menu and add it to the menubar
        view_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="View", menu=view_menu)
        lwlog.info("%s.%s"%(module,func),"Menu Bar Created")

    # Log stuff to TEXT in Program
    def log(self, s):
        func = "log"
        lwlog.info("%s.%s"%(module,func),"Logging to TEXT area")
        self.text.insert("end", s + "\n")
        self.text.see("end")
        self.text.pack()

    # Edit Menu
    def on_clear(self): 
        func = "on_clear"
        lwlog.info("%s.%s"%(module,func),"Clearing TEXT area")
        lwlog.crit()
        self.text.delete("1.0","end")

   # Exit program via close button
    def on_closing(self):
        func = "on_closing"
        lwlog.log_end('%s.%s'%(module,func))
        sys.exit(0)

    # Delete Database
    def on_delete(self):
        func = "on_delete"
        lwlog.warn('%s.%s'%(module,func),"Deleting databases")

        confirmtxt = "This will delete the database.\nThis is irreversable.\n\nAre you sure?"
        if msgbx.askokcancel("Recreate Database and Tables", confirmtxt, default="cancel", icon="warning"):
            print("Destroying and Recreating databases")
            mydb = db.db_openConnection("root", "1961@PJAnd3r50n")
            db.db_deleteDB(mydb.cursor(), dbName)
            db.db_closeConnection(mydb)

            lwlog.info('%s.%s'%(module,func),"   Deletion Successful")
            return True
        else:
            lwlog.info('%s.%s'%(module,func),"  DB Deletion Canceled")
            print("DB Deletion Cancelled")
            return False

    # List DB tables
    def on_list(self):
        func = "on_list"
        lwlog.info('%s.%s'%(module,func),"Listing DB Tables")

        dbName = 'LeatherWorks'
        dbUser = 'leatherworker'
        dbUserPWD = '1960@And3r50n'

        mydb = db.db_openConnection(dbUser, dbUserPWD)
        dbtableList = db.db_tablelist(mydb.cursor(), dbName)
        self.log('Database : ' + dbName)
        for table in dbtableList:
            self.log('  ' + ''.join(table))
        db.db_closeConnection(mydb)  

    # Exit program
    def on_quit(self): 
        func = "on_quit"
        lwlog.log_end('%s.%s'%(module,func))
        sys.exit(0)

    # Delete DB Tables and Database, and recreate them
    def on_recreate(self):
        func = "on_recreate"
        lwlog.warn('%s.%s'%(module,func),"Recreate Database and Tables")
        TABLES = {}
        TABLES['lwprojects'] = (
            "CREATE TABLE `lwprojects` ("
            "  `project_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `cost` decimal(10,2) NOT NULL,"
            "  `total_cost` decimal(10,2) NOT NULL,"
            "  `markup` decimal(10,2) NOT NULL,"
            "  `labor_hours` decimal(10,2) NOT NULL,"
            "  `sell_price` decimal(10,2) NOT NULL,"
            "  `adjusted` decimal(10,2) NOT NULL,"
            "  `profit` decimal(10,2) NOT NULL,"
            "  `hardware1_id` int(11) NOT NULL,"
            "  `hardware1_qty` decimal(10,2) NOT NULL,"
            "  `hardware2_id` int(11) NOT NULL,"
            "  `hardware2_qty` decimal(10,2) NOT NULL,"
            "  `hardware3_id` int(11) NOT NULL,"
            "  `hardware3_qty` decimal(10,2) NOT NULL,"
            "  `hardware4_id` int(11) NOT NULL,"
            "  `hardware4_qty` decimal(10,2) NOT NULL,"
            "  `hardware5_id` int(11) NOT NULL,"
            "  `hardware5_qty` decimal(10,2) NOT NULL,"
            "  `hardware6_id` int(11) NOT NULL,"
            "  `hardware6_qty` decimal(10,2) NOT NULL,"
            "  `hardware7_id` int(11) NOT NULL,"
            "  `hardware7_qty` decimal(10,2) NOT NULL,"
            "  `hardware8_id` int(11) NOT NULL,"
            "  `hardware8_qty` decimal(10,2) NOT NULL,"
            "  `hardware9_id` int(11) NOT NULL,"
            "  `hardware9_qty` decimal(10,2) NOT NULL,"
            "  `hardware10_id` int(11) NOT NULL,"
            "  `hardware10_qty` decimal(10,2) NOT NULL,"
            "  PRIMARY KEY (`project_id`)"
            ") ENGINE=InnoDB")

        TABLES['lwlabor'] = (
            "CREATE TABLE `lwlabor` ("
            "  `labor_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `annual_expnesies` decimal(10,2) NOT NULL,"
            "  `annual_sallary` decimal(10,2) NOT NULL,"
            "  `total_expenses` decimal(10,2) NOT NULL,"
            "  `work_weeks` decimal(2) NOT NULL,"
            "  `daily_hours` decimal(2) NOT NULL,"
            "  `days_per_week` decimal(1) NOT NULL,"
            "  `expenses_per_day` decimal(10,2) NOT NULL,"
            "  `shop_rate` decimal(10,2) NOT NULL,"
            "  PRIMARY KEY (`labor_id`)"
            ") ENGINE=InnoDB")

        TABLES['lwcosts'] = (
            "CREATE TABLE `lwcosts` ("
            "  `cost_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `cost` decimal(10,2) NOT NULL,"
            "  `total_cost` decimal(10,2) NOT NULL,"
            "  `markup` decimal(10,2) NOT NULL,"
            "  `labor_hours` decimal(10,2) NOT NULL,"
            "  `sell_price` decimal(10,2) NOT NULL,"
            "  `adjusted` decimal(10,2) NOT NULL,"
            "  `profit` decimal(10,2) NOT NULL,"
            "  PRIMARY KEY (`cost_id`)"
            ") ENGINE=InnoDB")

        TABLES['lwhardware'] = (
            "CREATE TABLE `lwhardware` ("
            "  `hardware_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `hardware_name` varchar(50) NOT NULL,"
            "  `hardware_cost_per_each` decimal(10,2) NOT NULL,"
            "  PRIMARY KEY (`hardware_id`)"
            ") ENGINE=InnoDB")
    
        confirmtxt = "THis will destroy all current data, delete and recreate the database.\nThis is unreversable.\n\nAre you sure?"
        if msgbx.askokcancel("Recreate Database and Tables", confirmtxt, default="cancel", icon="warning"):
            lwlog.info('%s.%s'%(module,func),"  Destroying and Recreating databases")
            print("Destroying and Recreating databases")
            mydb = db.db_openConnection("root", "1961@PJAnd3r50n")

            dbName = 'LeatherWorks'
            dbUser = 'leatherworker'
            dbUserPWD = '1960@And3r50n'

            print(TABLES)

            db.db_deleteDB(mydb.cursor(), dbName)
            db.db_createDB(mydb, dbName)
            db.db_createTables(mydb.cursor(), TABLES)
            db.db_grantUserPriv(mydb.cursor(), dbName, dbUser)
            db.db_closeConnection(mydb)

            lwlog.info('%s.%s'%(module,func),"  Destroying and Recreating databases Complete")
            return True
        else:
            lwlog.info('%s.%s'%(module,func),"  Recreated Cancelled")
            print("Recreated Cancelled")
            return False

#Main App loop
if __name__ == "__main__":
    if not os.path.exists('logging'):
        os.mkdir('logging')
    
    lwlog.log_begin("Leather Work Costing")
    app = costing()
    app.mainloop()

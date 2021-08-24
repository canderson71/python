#******************************
#
# NAME      : db_common.py
# AUthOR    : Chris Anderson
# EMAIL     : chris.anderson@andersonleatherworks.com
# DATE      : 08/18/2021
# PURPOSE   : This file contains all the Common database modules
#
#******************************

# Imports
import mysql.connector
import sys
from mysql.connector.cursor import MySQLCursorBufferedDict
from mysql.connector import errorcode
from common_package.alwlogger import ALWLogging as alwlog
from datetime import date

# Globals
global __mycursor
global __mydb
global __module

class DBCommon:
    __module = 'db_common'
    # Close database connection
    def _dbcloseConnection(__mydb):
        __module = 'db_common'
        func = '_dbcloseConnection'
        try:
            alwlog._info('%s.%s'%(__module, func), 'Closing DB Connection')
            __mydb.close    
        except mysql.connector.Error as err:
            alwlog._crit('%s.%s'%(__module, func), 'Closing MySQL Connection {}'.format(err.msg))
        else:
            alwlog._info('%s.%s'%(__module, func), 'Closed DB Connection')
    
    # Create database tables and grant rights to the internal user
    def _dbcreateDB(__mydb, dbName):
        __module = 'db_common'
        func = '_dbcreateDB'
        __mycursor = __mydb.cursor()
        try:
            alwlog._info('%s.%s'%(__module, func), 'Creating DBs')
            __mycursor.execute(
                'CREATE DATABASE IF NOT EXIStS {} DEFAULT CHARACTER SET "utf8"'.format(dbName))
        except mysql.connector.Error as err:
            alwlog._crit('%s.%s'%(__module, func), 'Failed creating database: {}'.format(err))
            exit(1)
        else:
            alwlog._info('%s.%s'%(__module, func), 'Created DBs')

        try:
            __mycursor.execute('USE {}'.format(dbName))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                DBCommon._dbcreateDB(__mycursor, dbName)
                __mydb.database = dbName
            else:
                exit(1)

    # Create database tables and grant rights to the internal user
    def _dbcreateTables(__mycursor, TABLES):
        __module = 'db_common'
        func = '_dbcreateTables'
        alwlog._info('%s.%s'%(__module, func), 'Creating DB Tables')
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                alwlog._info('%s.%s'%(__module, func), 'Creating table {}: '.format(table_name))
                __mycursor.execute(table_description)
            except mysql.connector.Error as err:
                alwlog._crit('%s.%s'%(__module, func), 'Failed creating table: {}'.format(err))
            else:
                alwlog._info('%s.%s'%(__module, func), 'Created table {}: '.format(table_name))

    # Create a database user
    def _dbcreatUser(__mycursor, dbUserName, password,
                querynum=0, 
                updatenum=0, 
                connection_num=0):

        __module = 'db_common'
        func = '_dbcreatUser'
        alwlog._info('%s.%s'%(__module, func), 'Creating user {}: '.format(dbUserName))
        try:
            sqlCreateUser = 'CREATE USER IF NOT EXISTs "%s"@"localhost" IDENTIFIED BY "%s";'%(dbUserName, password)
            __mycursor.execute(sqlCreateUser)
        except mysql.connector.Error as err:
            alwlog._crit('%s.%s'%(__module, func), 'Failed creating user: {}'.format(err))
        else:
            alwlog._info('%s.%s'%(__module, func), 'Created user {}: '.format(dbUserName))

    # Delete DB Table
    def _dbdeleteDB(__mycursor, dbName):
        __module = 'db_common'
        func = '_dbdeleteDB'
        alwlog._info('%s.%s'%(__module, func), 'Deleting DB {}: '.format(dbName))

        try:
            sqlDB = 'DROP DATABASE IF EXISTS %s'%(dbName)
            __mycursor.execute(sqlDB)
        except mysql.connector.Error as err:
            alwlog._crit('%s.%s'%(__module, func), 'Failed deleting DB: {}'.format(err))
        else:
            alwlog._info('%s.%s'%(__module, func), 'Deleted DB {}: '.format(dbName))

    # Delete DB User
    def _dbdeleteUser(__mycursor, dbUserName):
        __module = 'db_common'
        func = '_dbdeleteUser'
        alwlog._info('%s.%s'%(__module, func), 'Deleting DB User {}: '.format(dbName))
        try:
            alwlog._info('%s.%s'%(__module, func), 'Deleting User {}: '.format(dbUserName))
            sqlUser = 'DROP USER IF EXISTS %s'%(dbUserName)
            __mycursor.execute(sqlUser)
        except mysql.connector.Error as err:
            alwlog._crit('%s.%s'%(__module, func), 'Failed deleting DB User: {}'.format(err))
        else:
            alwlog._info('%s.%s'%(__module, func), 'Deleted DB User {}: '.format(dbName))

    # Grant DB User DB Privaleges
    def _dbgrantUserPriv(__mycursor, dbName, dbUser):
        __module = 'db_common'
        func = '_dbgrantUserPriv'
        alwlog._info('%s.%s'%(__module, func), 'Granting User Privaleges {}: '.format(dbName))
        try:
            sqlUser = 'GRANT ALL on %s.* to %s@localhost'%(dbName, dbUser)
            __mycursor.execute(sqlUser)
        except mysql.connector.Error as err:
            alwlog._crit('%s.%s'%(__module, func), 'Failed Granting User Privaleges: {}'.format(err))
        else:
            alwlog._info('%s.%s'%(__module, func), 'Granted User Privaleges {}: '.format(dbName))
        # commit results
        __mycursor.execute('Flush privileges')

    # Open DB Connection
    def _dbopenConnection(dbUserName, dbPasswd):
        __module = 'db_common'
        func = '_dbopenConnection'
        alwlog._info('%s.%s'%(__module, func), 'Opening DB Connection using {}: '.format(dbUserName))
        try:
            __mydb = mysql.connector.connect(
                host='localhost',
                user=dbUserName,
                password=dbPasswd
            )
        except mysql.connector.Error as err:
            alwlog._crit('%s.%s'%(__module, func), 'Failed Opening DB Connectiion : {}'.format(err))
        else:
            alwlog._info('%s.%s'%(__module, func), 'Opened DB Connection using {}: '.format(dbUserName))
        return (__mydb)

    # List DB Tables
    def _dbtablelist(__mycursor, dbName):
        __module = 'db_common'
        func = '_dbtablelist'
        alwlog._info('%s.%s'%(__module, func), 'Listing DB Tables')
        try:
            sql = 'SHOW TABLES IN %s'%(dbName)
            __mycursor.execute(sql)
            tables = __mycursor.fetchall()
            return (tables)
        except mysql.connector.Error as err:
            alwlog._crit('%s.%s'%(__module, func), 'Failed Listing DB Tables : {}'.format(err))
        else:
            alwlog._info('%s.%s'%(__module, func), 'Listed DB Tables')
 
# Main DB Section            
if __name__ == '__main__':
   print ('This is the db_common.py file' )  
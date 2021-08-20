#******************************
#
# NAME      : db_common.py
# AUthOR    : Chris Anderson
# EMAIL     : chris.anderson@andersonleatherworks.com
# DATE      : 08/18/2021
# PURPOSE   : This file contains all the common database modules
#
#******************************

# Imports
import mysql.connector
from mysql.connector.cursor import MySQLCursorBufferedDict
from mysql.connector import errorcode
from common_package.lwlogger import lwlogging as lwlog

# Globals
global mycursor
global mydb
global module

class dbcommon:
    module = "db_common"
    # Close database connection
    def db_closeConnection(mydb):
        module = "db_common"
        func = 'db_closeConnection'
        try:
            lwlog.info('%s.%s'%(module, func), "Closing DB Connection")
            print("Closing MySQL Connection {}: ", end='')
            mydb.close    
        except mysql.connector.Error as err:
            lwlog.crit('%s.%s'%(module, func), "Closing MySQL Connection {}".format(err.msg))
            print(err.msg)
        else:
            lwlog.info('%s.%s'%(module, func), "Closed DB Connection")
            print("OK")
    
    # Create database tables and grant rights to the internal user
    def db_createDB(mydb, dbName):
        module = "db_common"
        func = 'db_createDB'
        mycursor = mydb.cursor()
        try:
            lwlog.info('%s.%s'%(module, func), "Creating DBs")
            mycursor.execute(
                "CREATE DATABASE IF NOT EXIStS {} DEFAULT CHARACTER SET 'utf8'".format(dbName))
        except mysql.connector.Error as err:
            lwlog.crit('%s.%s'%(module, func), "Failed creating database: {}".format(err))
            print("Failed creating database: {}".format(err))
            exit(1)
        else:
            lwlog.info('%s.%s'%(module, func), "Created DBs")
            print("OK")

        try:
            mycursor.execute("USE {}".format(dbName))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(dbName))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                db_createDB(mycursor, dbName)
                print("Database {} created successfully.".format(dbName))
                mydb.database = dbName
            else:
                print(err)
                exit(1)

    # Create database tables and grant rights to the internal user
    def db_createTables(mycursor, TABLES):
        module = "db_common"
        func = 'db_createTables'
        lwlog.info('%s.%s'%(module, func), "Creating DB Tables")
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                lwlog.info('%s.%s'%(module, func), "Creating table {}: ".format(table_name))
                print("Creating table {}: ".format(table_name), end='')
                mycursor.execute(table_description)
            except mysql.connector.Error as err:
                lwlog.crit('%s.%s'%(module, func), "Failed creating table: {}".format(err))
                print(err.msg)
            else:
                lwlog.info('%s.%s'%(module, func), "Created table {}: ".format(table_name))
                print("OK")

    # Create a database user
    def db_creatUser(mycursor, dbUserName, password,
                querynum=0, 
                updatenum=0, 
                connection_num=0):

        module = "db_common"
        func = 'db_creatUser'
        lwlog.info('%s.%s'%(module, func), "Creating user {}: ".format(dbUserName))
        try:
            print("Creating user {}: ".format(dbUserName), end='')
            sqlCreateUser = "CREATE USER IF NOT EXISTs '%s'@'localhost' IDENTIFIED BY '%s';"%(dbUserName, password)
            mycursor.execute(sqlCreateUser)
        except mysql.connector.Error as err:
            lwlog.crit('%s.%s'%(module, func), "Failed creating user: {}".format(err))
            print(err.msg)
        else:
            lwlog.info('%s.%s'%(module, func), "Created user {}: ".format(dbUserName))
            print("OK")

    # Delete DB Table
    def db_deleteDB(mycursor, dbName):
        module = "db_common"
        func = 'db_deleteDB'
        lwlog.info('%s.%s'%(module, func), "Deleting DB {}: ".format(dbName))

        try:
            print("Deleting Database {}: ".format(dbName), end='')
            sqlDB = "DROP DATABASE IF EXISTS %s"%(dbName)
            mycursor.execute(sqlDB)
        except mysql.connector.Error as err:
            lwlog.crit('%s.%s'%(module, func), "Failed deleting DB: {}".format(err))
            print(err.msg)
        else:
            lwlog.info('%s.%s'%(module, func), "Deleted DB {}: ".format(dbName))
            print("OK")

    # Delete DB User
    def db_deleteUser(mycursor, dbUserName):
        module = "db_common"
        func = 'db_deleteUser'
        lwlog.info('%s.%s'%(module, func), "Deleting DB User {}: ".format(dbName))
        try:
            print("Deleting User {}: ".format(dbUserName), end='')
            sqlUser = "DROP USER IF EXISTS %s"%(dbUserName)
            mycursor.execute(sqlUser)
        except mysql.connector.Error as err:
            lwlog.crit('%s.%s'%(module, func), "Failed deleting DB User: {}".format(err))
            print(err.msg)
        else:
            lwlog.info('%s.%s'%(module, func), "Deleted DB User {}: ".format(dbName))
            print("OK")    

    # Grant DB User DB Privaleges
    def db_grantUserPriv(mycursor, dbName, dbUser):
        module = "db_common"
        func = 'db_grantUserPriv'
        lwlog.info('%s.%s'%(module, func), "Granting User Privaleges {}: ".format(dbName))
        try:
            print("Granting User Rights to {}: ".format(dbUser, dbName), end='')
            sqlUser = "GRANT ALL on %s.* to %s@localhost"%(dbName, dbUser)
            mycursor.execute(sqlUser)
        except mysql.connector.Error as err:
            lwlog.crit('%s.%s'%(module, func), "Failed Granting User Privaleges: {}".format(err))
            print(err.msg)
        else:
            lwlog.info('%s.%s'%(module, func), "Granted User Privaleges {}: ".format(dbName))
            print("OK")  
        # commit results
        mycursor.execute("Flush privileges")

    # Open DB Connection
    def db_openConnection(dbUserName, dbPasswd):
        module = "db_common"
        func = 'db_openConnection'
        lwlog.info('%s.%s'%(module, func), "Opening DB Connection using {}: ".format(dbUserName))
        try:
            print("Connecting to MySQL{}: ", end='')
            mydb = mysql.connector.connect(
                host="localhost",
                user=dbUserName,
                password=dbPasswd
            )
        except mysql.connector.Error as err:
            lwlog.crit('%s.%s'%(module, func), "Failed Opening DB Connectiion : {}".format(err))
            print(err.msg)
        else:
            lwlog.info('%s.%s'%(module, func), "Opened DB Connection using {}: ".format(dbUserName))
            print("OK") 
        return (mydb)

    # List DB Tables
    def db_tablelist(mycursor, dbName):
        module = "db_common"
        func = 'db_tablelist'
        lwlog.info('%s.%s'%(module, func), "Listing DB Tables")
        try:
            print("Getting list of DB Tables")
            sql = "SHOW TABLES IN %s"%(dbName)
            mycursor.execute(sql)
            tables = mycursor.fetchall()
            return (tables)
        except mysql.connector.Error as err:
            lwlog.crit('%s.%s'%(module, func), "Failed Listing DB Tables : {}".format(err))
            print(err.msg)
        else:
            lwlog.info('%s.%s'%(module, func), "Listed DB Tables")
            print("OK") 
 
# Main DB Section            
if __name__ == '__main__':
   print ('This is the db_common.py file' )  
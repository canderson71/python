import mysql.connector
from mysql.connector.cursor import MySQLCursorBufferedDict
from mysql.connector import errorcode

global mycursor
global mydb

def db_closeConnection(mydb):
    try:
        print("Closing MySQL Connection {}: ", end='')
        mydb.close    
    except mysql.connector.Error as err:
            print(err.msg)
    else:
        print("OK")
 
# Define a method to create database tables and grant rights to the internal user
def db_createDB(mydb, dbName):
    mycursor = mydb.cursor()
    try:
        mycursor.execute(
            "CREATE DATABASE IF NOT EXIStS {} DEFAULT CHARACTER SET 'utf8'".format(dbName))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
    else:
        print("OK")

    try:
        mycursor.execute("USE {}".format(dbName))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(dbName))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            db_createDB(mycursor)
            print("Database {} created successfully.".format(dbName))
            mydb.database = dbName
        else:
            print(err)
            exit(1)

# Define a method to create database tables and grant rights to the internal user
def db_createTables(mycursor, TABLES):
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            mycursor.execute(table_description)
        except mysql.connector.Error as err:
                print(err.msg)
        else:
            print("OK")

# Define a method to create a database user
def db_creatUser(mycursor, dbUserName, password,
               querynum=0, 
               updatenum=0, 
               connection_num=0):

        try:
            print("Creating user {}: ".format(dbUserName), end='')
            sqlCreateUser = "CREATE USER IF NOT EXISTs '%s'@'localhost' IDENTIFIED BY '%s';"%(dbUserName, password)
            mycursor.execute(sqlCreateUser)
        except mysql.connector.Error as err:
                print(err.msg)
        else:
            print("OK")

# Delete DB Table
def db_deleteDB(mycursor, dbName):

    try:
        print("Deleting Database {}: ".format(dbName), end='')
        sqlDB = "DROP DATABASE IF EXISTS %s"%(dbName)
        mycursor.execute(sqlDB)
    except mysql.connector.Error as err:
            print(err.msg)
    else:
        print("OK")

def db_deleteUser(mycursor, dbUserName):
    try:
        print("Deleting User {}: ".format(dbUserName), end='')
        sqlUser = "DROP USER IF EXISTS %s"%(dbUserName)
        mycursor.execute(sqlUser)
    except mysql.connector.Error as err:
            print(err.msg)
    else:
        print("OK")    

def db_grantUserPriv(mycursor, dbName, dbUser):
    try:
        print("Granting User Rights to {}: ".format(dbUser, dbName), end='')
        sqlUser = "GRANT ALL on %s.* to %s@localhost"%(dbName, dbUser)
        mycursor.execute(sqlUser)
    except mysql.connector.Error as err:
            print(err.msg)
    else:
        print("OK")  
    # commit results
    mycursor.execute("Flush privileges")

def db_openConnection():
    try:
        print("Connecting to MySQL{}: ", end='')
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1961@PJAnd3r50n"
        )
    except mysql.connector.Error as err:
            print(err.msg)
    else:
        print("OK") 
    return (mydb)

# Define a method to create a database connection
def db_initialize(Tables):
    mydb = db_openConnection()

    dbName = 'LeatherWorks'
    dbUser = 'leatherworker'
    dbUserPWD = '1960@And3r50n'

    db_createDB(mydb, dbName)
    db_createTables(mydb.cursor(), TABLES)
    db_creatUser(mydb.cursor(), dbUser, dbUserPWD)
    db_grantUserPriv(mydb.cursor(), dbName, dbUser)
    db_deleteUser(mydb.cursor(), dbUser)
    db_deleteDB(mydb.cursor(), dbName)
    db_closeConnection(mydb)

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
    "CREATE TABLE `llwabor` ("
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

db_initialize(TABLES)

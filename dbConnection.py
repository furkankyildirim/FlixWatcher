#: Imports
import mysql.connector
from configparser import ConfigParser


#: Get Configs
config = ConfigParser()
config.read("config.ini")

#: Create the connection
mydb = mysql.connector.connect(user=config["Database"]["user"], password=config["Database"]["pass"],
                               host=config["Database"]["host"], database=config["Database"]["db"])

#: Create the cursor
mycursor = mydb.cursor()

#: Create table if not exists
mycursor.execute("CREATE TABLE IF NOT EXISTS Movies (id BIGINT, Name TEXT, Description TEXT, Type TEXT, Year TEXT, Rating TEXT, Director TEXT, Genres TEXT, Image LONGBLOB, startDate TEXT, endDate TEXT, webLink TEXT, netflixLink TEXT, Duration TEXT);")
mycursor.execute("CREATE TABLE IF NOT EXISTS Preview (id BIGINT, Name TEXT, Type TEXT, Year TEXT, Image LONGBLOB);")
mycursor.execute("CREATE TABLE IF NOT EXISTS Persons (id BIGINT, Name TEXT, Movies JSON, webLink TEXT, netflixLink TEXT);")

mycursor.close()


# method: dbExecute
# Executes a statement
# @sql, str: The execution statement
# @params, tuple: Arguments
# @completed
def dbExecute(sql: str, params: tuple):
    cursor = mydb.cursor()
    cursor.execute(sql, params)
    mydb.commit()
    cursor.close()


# method: dbSelect
# Executes a statement for selecting
# @sql, str: The execution statement
# @params, tuple: Arguments
# @return: Output
# @completed
def dbSelect(sql: str, params: tuple):
    cursor = mydb.cursor()
    cursor.execute(sql, params)
    myresult = cursor.fetchall()
    cursor.close()

    return myresult


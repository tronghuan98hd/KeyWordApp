import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
import mysql.connector
import pymysql.cursors
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = myclient["bhxh"]
col = db["keyword"]
user = 'root'
passw = 'huan1998'
host = 'localhost'
port = 3306
database = 'intent_keyword'

mydb = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passw,
    database=database,
    auth_plugin='mysql_native_password',
)

mycursor = mydb.cursor()

select_query = "SELECT id,name FROM post_keyword"

sel_query = select_query
mycursor.execute(sel_query)
myresult = mycursor.fetchall()

for result in myresult:
    mydict = {"keyword": result[1]}
    x = col.insert_one(mydict)
    print(x.inserted_id)

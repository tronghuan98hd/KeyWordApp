import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
import mysql.connector
import pymysql.cursors

user = 'root'
passw = 'huan1998'
host = 'localhost'
port = 3306
database = 'intent_keyword'

df = pd.read_csv('intents_keywords.txt', usecols=[
                 'intentId', 'intent', 'keyword'], sep=",", encoding='utf-8')
keyword = df['keyword'].values
intent = df['intent'].values
intentId = df['intentId'].values

intent_query = "INSERT INTO post_intent(intentId, intent) VALUES"
keyword_query = "INSERT INTO post_keyword(name, intent_id) VALUES"

mydb = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passw,
    database=database,
    auth_plugin='mysql_native_password',
)

mycursor = mydb.cursor()
keyArr = []
try:
    for i in range(0, df.shape[0]-1):
        query = intent_query + """("%s", "%s");""" % (intentId[i], intent[i])
        mycursor.execute(query)
        keyArr = keyword[i].split('; ')
        for key in keyArr:
            query = keyword_query + """("%s", "%s");""" % (key, intentId[i])
            mycursor.execute(query)
except:
    print("Something went wrong when writing to the file")

mydb.commit()
mydb.close()
# for i in range(0, df.shape[0]-1):
#     query = intent_query + """("%s", "%s");""" % (intentId[i], intent[i])
#     mycursor.execute(query)
#     keyArr = keyword[i].split('; ')
#     for key in keyArr:
#         query = keyword_query + """("%s", "%s");""" % (key, intentId[i])
#         mycursor.execute(query)

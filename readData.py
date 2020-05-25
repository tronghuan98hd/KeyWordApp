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
keyword_query = "INSERT INTO post_keyword(name) VALUES"
key_intent_query = "INSERT INTO post_key_intent(intent_id, keyword_id) VALUES"
select_query = "SELECT id,name FROM post_keyword WHERE name LIKE "

mydb = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passw,
    database=database,
    auth_plugin='mysql_native_password',
)

mycursor = mydb.cursor()
keyArr = []

for i in range(0, df.shape[0]-1):
    # query = intent_query + """("%s", "%s");""" % (intentId[i], intent[i])
    # mycursor.execute(query)
    # keyArr += keyword[i].split('; ')
    keyArr = keyword[i].split('; ')
    for key in keyArr:
        #     query = keyword_query + """("%s", "%s");""" % (key, intentId[i])
        #     mycursor.execute(query)
        print(key)
        sel_query = select_query + """CONVERT("%s", BINARY);""" % (key)
        mycursor.execute(sel_query)
        myresult = mycursor.fetchall()
        print(myresult[0][1])
        query = key_intent_query + \
            """("%s", %s);""" % (intentId[i], myresult[0][0])
        mycursor.execute(query)

keySet = set(keyArr)

for key in keySet:
    query = keyword_query + """("%s");""" % (key)
    mycursor.execute(query)


mydb.commit()
mydb.close()

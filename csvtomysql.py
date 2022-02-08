import pandas as pd
empdata = pd.read_csv('File 3.csv',header=None,index_col=False, delimiter = ',',skiprows=1)
empdata.head()
import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='chandana',password='chandana@2022',db='production')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        #cursor.execute('DROP TABLE IF EXISTS daily_production;')
        print('Creating table....')
        #cursor.execute("CREATE TABLE daily_production(TimeStamp varchar(225) ,User_ID varchar(225),Prd_ID varchar(225),Attrib_1 varchar(225),Attrib_2 varchar(225),Attrib_3 varchar(225),Attrib_4 varchar(225),Attrib_5 varchar(225),Attrib_6 varchar(225),Attrib_7 varchar(225))")
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO production.daily_production VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)
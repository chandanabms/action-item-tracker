import csv
import os
import mysql.connector
import xlrd
with open('table_struvture.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter = ',')
	list_of_column_names = []
	for row in csv_reader:
		list_of_column_names.append(row)
		break
print(list_of_column_names[0])
# path = r"/home/chandana/Desktop/Projects/Python/DailyProcess/07-02-2022"
# directories = os.listdir(path)
# list_img=[]
# for file in directories:
# 	list_img.append(file)
# print(list_img)
import pandas as pd
import glob # getting excel files from Directory Desktop 
path = "/home/chandana/Desktop/Projects/Python/DailyProcess/07-02-2022" # read all the files with extension .xlsx i.e. excel 
filenames = glob.glob(path + "/*.xlsx") 
print('File names:', filenames) # for loop to iterate all excel 
for file in filenames: # reading excel files 
	print("Reading file = ",file) 
	print(pd.read_excel(file))
conn = mysql.connector.connect(user='chandana', password='chandana@2022', host='localhost', database='production')
mycursor = conn.cursor()
# mycursor.execute("CREATE TABLE IF NOT EXISTS daily_production(TimeStamp int ,User_ID varchar(225),Prd_ID varchar(225),Attrib_1 varchar(225),Attrib_2 varchar(225),Attrib_3 varchar(225),Attrib_4 varchar(225),Attrib_5 varchar(225),Attrib_6 varchar(225),Attrib_7 varchar(225))")

import pymysql
pymysql.install_as_MySQLdb
import MySQLdb
conn = mysql.connector.connect(user='chandana', password='chandana@2022', host='localhost',database='production')
mycursor = conn.cursor()
excel_sheet = xlrd.open_workbook('File 1.xlsx')
print(excel_sheet)
sheet_name = excel_sheet.sheet_names()
print(sheet_name)
query = "INSERT INTO daily_production(TimeStamp,User_ID ,Prd_ID ,Attrib_1,Attrib_2 ,Attrib_3,Attrib_4 ,Attrib_5 ,Attrib_6 ,Attrib_7) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for sh in range(0,len(sheet_number)):
	sheet = excel_sheet.sheet_by_index(sh)
	for r in range(1,sheet.nrows):
		TimeStamp = sheet.cell(r,0).value
		User_ID = sheet.cell(r,1).value
		Prd_ID = sheet.cell(r,2).value
		Attrib_1 = sheet.cell(r,3).value
		Attrib_2 = sheet.cell(r,4).value
		Attrib_3 = sheet.cell(r,5).value
		Attrib_4 = sheet.cell(r,6).value
		Attrib_5 = sheet.cell(r,7).value
		Attrib_6 = sheet.cell(r,8).value
		Attrib_7 = sheet.cell(r,9).value
		production_value = (TimeStamp,User_ID ,Prd_ID ,Attrib_1,Attrib_2 ,Attrib_3,Attrib_4 ,Attrib_5 ,Attrib_6 ,Attrib_7)
		mycursor.execute(query,production_value)
		conn.commit()
		mycursor.close()
		conn.close()
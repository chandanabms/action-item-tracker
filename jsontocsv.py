import json
import csv
with open('op2.json') as json_file:
	data = json.load(json_file)
employee_data = data #to save json data
data_file = open('data_file.csv', 'w')
csv_writer = csv.writer(data_file)
count = 0
for emp in employee_data:
	if count == 0:
		header = emp.keys()#for heading
		csv_writer.writerow(header)
		count += 1
	csv_writer.writerow(emp.values()) #for values
data_file.close()
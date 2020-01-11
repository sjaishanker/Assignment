import MySQLdb
import csv
fields=[]
connection = MySQLdb.connect(host='localhost',user='root',db='test')
cursor=connection.cursor()
with open('dataset2.csv','r') as csvfile:
	csvreader=csv.reader(csvfile)
	next(csvreader)
	for row in csvreader:
		print(row)
		sql = "INSERT INTO t2 (ID, Office_ID, Population) VALUES (%s,%s,%s)"
		cursor.execute(sql,(int(row[0]),row[1],int(row[2])))
		connection.commit()
print("Committed")
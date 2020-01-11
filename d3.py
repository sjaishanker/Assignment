import MySQLdb
from flask import Flask 
app = Flask(__name__) 
@app.route('/') 
def main():
	connection = MySQLdb.connect(host='localhost',user='root',db='test')
	cursor=connection.cursor()
	SQL="use test;"
	cursor.execute(SQL)
	SQL="select * from t4;"
	cursor.execute(SQL)
	results=cursor.fetchall()
	return str(results)
if __name__ == '__main__':  
	app.run(port=8000) 

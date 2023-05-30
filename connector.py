import psycopg2

def inserting_data(fname,lname=None,age=None,sex=None,income=None):
   conn = psycopg2.connect(
   database="psql_connector", user='postgres', password='1010', host='127.0.0.1', port= '5432'
   )
   cursor = conn.cursor() 
   cursor.execute('insert into employee(first_name,last_name,age,sex,income) values (%s,%s,%s,%s,%s)',(fname,lname,age,sex,income))
   conn.commit()
   conn.close()

def display():
   conn = psycopg2.connect(
   database="psql_connector", user='postgres', password='1010', host='127.0.0.1', port= '5432'
   )
   cursor = conn.cursor()
   cursor.execute('select * from employee')
   data = cursor.fetchall()
   for i in data:
      print(i)
   conn.commit()
   conn.close() 
display()
import psycopg2

def display():
   conn = psycopg2.connect(
   database="data_jsonify", user='postgres', password='1010', host='127.0.0.1', port= '5432'
   )
   cursor = conn.cursor()
   cursor.execute('select * from "User";')
   data = cursor.fetchall()
   for i in data:
      print(i)
   conn.commit()
   conn.close() 
display()
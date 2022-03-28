from connection import connect_to_postgres
from select import select
import os
import env
if __name__ == '__main__':
  conn = connect_to_postgres(
  user=os.getenv('USER'),            
  password=os.getenv('PASSWORD'),
  host=os.getenv('HOST'),
  port=os.getenv('PORT'),             
  db=os.getenv('DB')
  )
  
  cursor = conn.cursor()
  
  print(select(cursor, "*", "productos"))

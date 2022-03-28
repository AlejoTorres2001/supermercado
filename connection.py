import psycopg2
from psycopg2 import Error

def connect_to_postgres(user,password,host,port,db):
  try:
    # Connect to an existing database
    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=db)
    return connection
  except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
    return None
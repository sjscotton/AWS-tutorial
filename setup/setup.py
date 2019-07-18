import psycopg2
import json


connection = psycopg2.connect(
)



cursor = connection.cursor()

if connection:
  cursor.execute(('''SELECT * FROM public.test_project_name'''))
  result = cursor.fetchone()
  print(result)
  print('connect')
  connection.close()
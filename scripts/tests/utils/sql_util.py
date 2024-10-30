import os
import logging
import sqlite3

def test_sql_read(dir_location):
   try:
    #  dir_location = "/efs/fim-data/ripple/prototype/2024_07_31"
     os.chdir(dir_location)
     assert os.getcwd() == dir_location, "Failed to load the directory" + dir_location
     dir_contents = sorted(os.listdir()) 
     print(dir_contents)    
     connection = sqlite3.connect('library.sqlite')
     cursor = connection.cursor()
     cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
     tables = cursor.fetchall()
     for table in tables:
       cursor.execute(f"SELECT * FROM {table[0]} LIMIT 10;")
       records = cursor.fetchall()
       for record in records:
          print(record)
       cursor.execute(f"SELECT COUNT(*) FROM {table[0]};")
       number_of_records = cursor.fetchone()[0]
       assert number_of_records > 0, "No records found"
     connection.close()
   except Exception as e:
      logging.error("Unexpected error/File Not found")
      raise e

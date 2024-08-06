import os
import logging

# value = 58
# expected_value = 'DFO-5678'
# text_file = '/efs/demonstrations/dfo_event_list.txt'

def extract_txt_data(text_file,total_records):
 
    try:
      with open(text_file,'r') as file:
        number_of_records = sum(1 for line in file)
        assert number_of_records == int(total_records) , "Value not correct"
        logging.info(f"Expected number of records present: {str(number_of_records)}")
    except Exception as e:
      logging.error("Unexpected error/File Not found")
      raise e         
    except AssertionError as e:
      logging.error("Record not found")
      raise e


def check_txt_data(text_file,expected_record_value):

    try:
      with open(text_file,'r') as file:
        for line in file:
          words = line.strip()
          print(words)
          print(expected_record_value)
          if words == expected_record_value:
            assert words == expected_record_value , "Record not found"
            logging.info("Expected record present")
            break
          raise ValueError(f"Value not found")
          logging.error("Data not found")
    except Exception as e:
      logging.error("Unexpected error/File Not found")
      raise e  
    except AssertionError as e:
      logging.error("Record not found")
      raise e

      
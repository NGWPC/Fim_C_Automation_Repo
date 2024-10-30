import os
import logging

def test_vrt_data(source_vrt_file,output_vrt_file):
   try:
     with open(source_vrt_file, 'r') as file1, open(output_vrt_file, 'r') as file2:
      file1_content = file1.read()
      file2_content = file2.read()
      if file1_content == file2_content:
         logging.info(f"Both VRT files are same: {file1} and {file2}")
   except Exception as e:
      logging.error("Unexpected error/File Not found")
      raise e

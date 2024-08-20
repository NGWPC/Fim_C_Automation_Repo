# tests/helpers.py

import os
from .utils import qgis_util,gpkg_util
import logging
import pexpect

def validate_geo_data(dir_path,output_file,expected_data_file,data_file_location):
   try:
      assert os.path.isdir(dir_path) == True , "Directory1 does not exist"+dir_path
      assert os.path.exists(dir_path) == True , "Directory does not exist"+dir_path

      # print(f"current working directory: {os.getcwd()}")

      dir_contents = sorted(os.listdir())
      file_path = os.path.join(dir_path,output_file)
      assert os.path.isfile(file_path) == True , "File does not exist"
   
      # qgis_util.test_run(dir_path, output_file,expected_data_file)
      gpkg_util.compare_gpkgs(file_path,data_file_location)
   except AssertionError as e:
      logging.error("Assertion failed for directory %s: %s",file_path)
      raise e


def validate_directories_files(directory_locations, directory_contents):
   for i,dir_location in enumerate(directory_locations):
      
      try:
         os.chdir(dir_location)
         assert os.getcwd() == dir_location, "Failed to load the directory" + dir_location
         dir_contents = sorted(os.listdir())     
         assert dir_contents == directory_contents[i], "Expected files not listed"
         logging.info("Expected files listed in %s", dir_location)
      except AssertionError as e:
         logging.error("Assertion failed for directory %s: %s", dir_location,e)
         raise e

# def remove_file(folder_name , data_file , file_name_path):
#       with open(os.path.join(os.path.dirname(__file__),folder_name,data_file), 'r') as file:
#             scenario = json.load(file)
#             shell_script = scenario['additional_data'][0].get('remove_file_shell_script')
#             result = subprocess.run(['bash',shell_script ,file_name_path ],stdout = subprocess.PIPE, universal_newlines = True)


def generate_dfo_data():
    child= pexpect.spawn('bash -c "source /efs/demonstrations/rs_stac_test/get_rs_stac_data.sh"')
    child.expect("Enter the event id:")
    child.sendline("4230\r")
    child.interact()

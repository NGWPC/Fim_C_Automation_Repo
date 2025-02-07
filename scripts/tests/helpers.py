# tests/helpers.py

import os
import requests
import json
import jsondiff
from dotenv import dotenv_values

from .utils import qgis_util
import logging
import pexpect



def validate_directories_files(directory_locations, directory_contents,flag): #,flag
 
      try:
        if flag=="partly":
           for dir_location,file in zip(directory_locations,directory_contents):
            for sub_file in file:
               print(sub_file)
               file_path = os.path.join(dir_location,str(sub_file))
               assert  os.path.isfile(file_path), f"{file} is not present"
        else:
           for i,dir_location in enumerate(directory_locations):
            os.chdir(dir_location)
            assert os.getcwd() == dir_location, "Failed to load the directory" + dir_location
            dir_contents = sorted(os.listdir()) 
            print(dir_contents)    
            assert dir_contents == directory_contents[i], "Expected files not listed"
            logging.info("Expected files listed in %s", dir_location)
      except AssertionError as e:
         logging.error("Assertion failed for directory %s: %s", dir_location,e)
         raise e

def generate_dfo_data():
    child= pexpect.spawn('bash -c "source /efs/demonstrations/rs_stac_test/get_rs_stac_data.sh"')
    child.expect("Enter the event id:")
    child.sendline("4230\r")
    child.interact()



def verify_gfm_data():
   print('I am here')
   
   chrome_options = webdriver.ChromeOptions()
   chrome_options.binary_location = "/usr/bin/chromium-browser"
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument("--disable-dev-shm-usage")
   print('I am here too')

   driver = webdriver.Chrome(executable_path = ChromeDriverManager().install(),options=chrome_options)
   driver.get('localhost:8080')
   page_url = driver.current_url
   print(page_url)


def validate_response(link,headers,data,destination_response_location):
   try:
      source_response = None
      destination_response = None
      response = requests.post(link,headers=headers , data =json.dumps(data))
      try:
         response.raise_for_status()
         if response.status_code == 200:
            source_response = response.json()
      except requests.exceptions.HTTPError as errh:
         print(f"Bad response: {response.status_code}")
         raise errh
      except requests.exceptions.ConnectionError as errc:
         print("Conection error: " ,errc)
         raise errc
      with open(destination_response_location, "r") as file:
         destination_response = json.load(file)
      # diff = jsondiff.diff(source_response,destination_response)
      # with open('diff_response.txt','w') as diff_file:
      #    diff_file.write(str(diff))
      assert source_response == destination_response , "source_response and destination_response rdoes not esponses match"
      logging.info("source_response and destination_response responses match")
   except AssertionError as e:
      logging.error("source_response and destination_response responses do not match")
      raise e
   

def verify_environment_variables(env_file,expected_content):
   try:
     env_values = dotenv_values(env_file)
     for key,expected_value in expected_content.items():
         actual_value = env_values.get(key)
         assert actual_value is not None , f"Missing {key}"
         print(actual_value)
         print(expected_value)
         assert str(actual_value) == str(expected_value),"Expected value not present"
         logging.info(f"{actual_value} is present as {expected_value} in the {env_file}")
   except AssertionError as e:
      logging.error(f"Expected value not present due to {e}")
      raise e
    
   


   

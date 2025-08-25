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
               print(file_path)
               assert  os.path.isfile(file_path), f"{file} is not present"
        elif flag=="partly_dir":
            for dir_location,file in zip(directory_locations,directory_contents):
             for sub_file in file:
               print(sub_file)
               file_path = os.path.join(dir_location,str(sub_file))
               print(file_path)
               assert  os.path.isdir(file_path), f"{file} is not present"
        else:
           for i,dir_location in enumerate(directory_locations):
            os.chdir(dir_location)
            assert os.getcwd() == dir_location, "Failed to load the directory" + dir_location
            dir_contents = sorted(os.listdir()) 
            print(dir_contents)  
            print(directory_contents[i])  
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

   chrome_options = webdriver.ChromeOptions()
   chrome_options.binary_location = "/usr/bin/chromium-browser"
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument("--disable-dev-shm-usage")
 

   driver = webdriver.Chrome(executable_path = ChromeDriverManager().install(),options=chrome_options)
   driver.get('localhost:8080')
   page_url = driver.current_url
   print(page_url)

def validate_downloaded_content(link,output_file):
   try:
      source_response = None
      destination_response = None
      response = None
      response = requests.get(link, stream = True)
      try:
         # output_file = "/home/jyoti.mikkilineni/Downloads/NA_E066N042T3_ENSEMBLE_OBSWATER_20250315T135747_VV_NA020M_E066N042T3_20250315.tif"
         response.raise_for_status()
         print(str(response.status_code))
         print(response.headers.get("Content-Type"))
         if response.status_code == 200:
            print('Success')
            with open(output_file, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                  f.write(chunk)
      except requests.exceptions.HTTPError as errh:
         print(f"Bad response: {response.status_code}")
         raise errh
      except requests.exceptions.ConnectionError as errc:
         print("Conection error: " ,errc)
         raise errc
   except AssertionError as e:
      logging.error("source_response and destination_response responses do not match")
      raise e

def validate_response(link,headers,data,destination_response_location):
   try:
      source_response = None
      destination_response = None
      response = None
      response = requests.get(link,headers=headers , data =json.dumps(data))
      try:
         response.raise_for_status()
         if response.status_code == 200:
            source_response = response.json()
         downloads_folder = os.path.join(os.getcwd(),"Downloads")
         file_path1 = os.path.join(downloads_folder,"response.json")
         with open(file_path1, "w", encoding = "utf-8") as f:
            json.dump(source_response, f, indent=4 , ensure_ascii=False)
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
      logging.info(f"{source_response} and {destination_response} responses match")
   except AssertionError as e:
      logging.error(f"{source_response}  responses do not match")
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

def file_exists_and_not_empty(file_path,file_type):
   assert os.path.exists(file_path) , f"{file_type.upper()} file missing : {file_path}"
   assert os.path.getsize(file_path)>0 , f"{file_type.upper()} file is empty : {file_path}"
    
   


   

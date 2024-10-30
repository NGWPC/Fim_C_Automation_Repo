# tests/helpers.py

import os
import requests
import json
import jsondiff
from .utils import qgis_util,gpkg_util
import logging
import pexpect
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

metrics_page_title = (By.XPATH,'//h1[@id="cross-site-contingency-metrics"]')
metrics_page_link='http://127.0.0.1:3000'
benchmark_category_field_xpath = '//label[@for="inputs-3a86ea-4"]//b'
table_header_xpath = '//*[@id="inputs-3a86ea-8"]//table//tr//th[2]'
benchmark_category_xpath = '//select[@id="inputs-3a86ea-4"]'
comp_version_xpath = '//select[@id="inputs-3a86ea-9"]'
plot_type_xpath = '//select[@id="inputs-3a86ea-1"]'
plot_type_label_xpath = '//*[@for="inputs-3a86ea-1"]/b'
contingency_metric_xpath = '//select[@id="inputs-3a86ea-2"]'
# dot_plot_type_xpath = '//*[@class="plot-d6a7b5"]//*[@aria-label="dot"][1]//*[@cx="475"][1]'
box_plot_type_xpath = '//*[@class="plot-d6a7b5"]//*[@aria-label="bar"][1]//*[@cx="55"]'
dot_plot_type_xpath = (By.XPATH,'//*[@class="plot-d6a7b5"]//*[@aria-label="dot"][1]//*[@cx="475"][1]')

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
      logging.error("Assertion failed for directory %s: %s",file_path,e)
      raise e


def validate_directories_files(directory_locations, directory_contents):
   for i,dir_location in enumerate(directory_locations):
      
      try:
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

def dropdown_selection(driver,val,element_xpath):
   page_element = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,element_xpath)))
   page_element_dropdown = Select(page_element)
   page_element_dropdown.select_by_visible_text(val)

def fields_validation(driver,field_xpath,field_text):
    
   webpage_field = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,field_xpath)))
   assert f"{field_text}" in webpage_field.text,f"{field_text} field validated"
   logging.info(f"{field_text} is displayed")


def verify_STAC_dashboard():

   chrome_options = Options()
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument("--disable-dev-shm-usage")
  

   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
   driver.get(metrics_page_link)
   page_url = driver.current_url
   print(f"current url is {page_url}")
   page_title = driver.find_element(*metrics_page_title)
   assert "Cross-site contingency" in page_title.text,"Page title is not found"

   fields_validation(driver,benchmark_category_field_xpath,"Benchmark category")
   dropdown_selection(driver,"ble",benchmark_category_xpath)
   fields_validation(driver,table_header_xpath,"huc")

   table_rows = 4
   table_columns = [2,4]
   for row in range(1,table_rows+1):
      for col in table_columns:
            cell_xpath = f"//*[@id='inputs-3a86ea-8']//table//tbody//tr[{row}]//td[{col}]"
            cell_value = driver.find_element(By.XPATH,cell_xpath)
            if ((row ==1 or row == 2) and col == 2):
               assert cell_value.text == '11090203',"Incorrect value displayed"
            elif ((row ==1 or row == 3) and col == 4):
               assert cell_value.text == '500yr',"Incorrect value displayed"
            elif ((row ==2 or row == 4) and col == 4):
               assert cell_value.text == '100yr',"Incorrect value displayed"
            elif ((row ==3 or row == 4) and col == 2):
               assert cell_value.text == '11090202',"Incorrect value displayed"
   print("Assertion successful")
   ###################Dot plot type verification#################################
   dropdown_selection(driver,"fim_4_4_0_0",comp_version_xpath)
   dropdown_selection(driver,"dots",plot_type_xpath)
   dropdown_selection(driver,"EQUITABLE_THREAT_SCORE",contingency_metric_xpath)
   dot_element = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@class="plot-d6a7b5"]//*[@aria-label="dot"][1]//*[@cx="475"][1]')))
   assert dot_element.is_displayed(), "Dot format is not displayed"
   logging.info("Dot plot type is displayed")

   ###################Box plot type verification#################################
   fields_validation(driver,plot_type_label_xpath,"Plot type:")
   driver.implicitly_wait(10)
   dropdown_selection(driver,"fim_4_5_2_0",comp_version_xpath)
   driver.implicitly_wait(10)
   dropdown_selection(driver,"box",plot_type_xpath)
   dropdown_selection(driver,"false_negatives_count",contingency_metric_xpath)
   driver.implicitly_wait(20)
   box_element = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@class="plot-d6a7b5"]//*[@aria-label="bar" and @fill="rgb(0,255,0)"]')))
   assert box_element.is_displayed(), "Box format is not displayed"
   logging.info("Box plot type is displayed")

   driver.quit()

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
   
   


   

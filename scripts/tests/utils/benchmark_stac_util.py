import os
import requests
import json
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium .common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

metrics_page_title = (By.XPATH,'//h1[@id="cross-site-contingency-metrics"]')
stac_api_browser_page_title = (By.XPATH,'//h1')
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
asset_download = (By.XPATH,"//div[@id='asset-E078N024T3_Observed_Water_Extent']//a[text()='Download']")
asset_copy = (By.XPATH,"//div[@id='asset-E078N024T3_Observed_Water_Extent']//button[text()=' Copy URL']")
asset_map_view = (By.XPATH,"//div[@id='asset-E078N024T3_Observed_Water_Extent']//button[text()=' Show on map ']")


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
            print(directory_locations)
            os.chdir(dir_location)
            assert os.getcwd() == dir_location, "Failed to load the directory" + dir_location
            dir_contents = sorted(os.listdir()) 
            print(dir_contents)    
            assert dir_contents == directory_contents[i], "Expected files not listed"
            print(directory_contents[i])
            logging.info("Expected files listed in %s", dir_location)
      except AssertionError as e:
         logging.error("Assertion failed for directory %s: %s", dir_location,e)
         raise e

def  verify_gfm_data(stac_link, gfm_item_name):
 
   chrome_options = webdriver.ChromeOptions()
   chrome_options.binary_location = "/usr/bin/chromium-browser"
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument("--disable-dev-shm-usage")
   service=Service("/usr/bin/chromedriver")
   driver =  webdriver.Chrome(service = service ,options=chrome_options)
   driver.get(stac_link)
   page_url = driver.current_url
   print(page_url)
   print(driver.title)
   while True:
      page_state = driver.execute_script("return document.readyState;")
      if page_state == "complete":
          break
   print(driver.page_source)
   wait = WebDriverWait(driver,20)
   # benchmark_stac_header = driver.find_element(By.TAG_NAME,'h1')
   benchmark_stac_header = driver.find_element(By.XPATH,"//h1//span[text()='stac-fastapi']")
   print(benchmark_stac_header.text)
   try:
     print("check1")
     element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/collections/gfm-expanded-collection']")))
     print("check2")
     print("Element found")
     ############# Navigation to Expanded Global Flood Monitoring Collection listing page ##############
     element.click()
     updated_link = driver.current_url
     print(updated_link)
   #   assert "Expanded Global Flood Monitoring Collection" in benchmark_stac_header.text,"Item not found"
    #############Search the item #################
     search_button = driver.find_element(By.XPATH,"//a[@title='Search']")
     search_button.click()
     item_search_input = driver.find_element(By.ID,"ids3")
     item_search_input.send_keys(gfm_item_name)
     item_search_input.send_keys(Keys.ENTER)
     driver.find_element(By.XPATH, "//button[text()='Submit']")
     searched_item = driver.find_element(By.XPATH,"//a[@class='stac-link stretched-link]")
     searched_item.click()
  #    ################Navigated to assets page##########################################
     assert gfm_item_name in benchmark_stac_header.text,"Item not found"
     asset_item = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@aria-controls = 'asset-E078N024T3_Observed_Water_Extent']")))
     asset_item.click()
     asset_download_option = driver.find_element(*asset_download)
     asset_copy_url_option = driver.find_element(*asset_copy)
     asset_copy_url_option = driver.find_element(*asset_map_view)

  #    ###########################Obtain the downloaded file #################################################
     asset_download_option.click()
     driver.quit()
    
   except TimeoutException:
     print("check3")
     print("Element not found")

   

  #  #page_title = driver.find_element(By.XPATH,'//h1//span[text()="stac-fastapi"]')
  #  #assert "stac-fastapi" in page_title.text,"Page title is not found"
  #  #item = driver.find_element(By.XPATH,'//a[@href="/collections/gfm-expanded-collection"]')
  #  #assert "Expanded Global Flood Monitoring Collection" in item.text,"Item not found"


  #  link = 'http://0.0.0.0:8000/gfm-expanded-collection/GFM-expanded_S1A_IW_GRDH_1SDV_20241123T005232_20241123T005257_056675_06F41A_B97A/NA_E078N024T3_ENSEMBLE_OBSWATER_20241123T005232_VV_NA020M_E078N024T3_20241123.tif'
  #  try:

  #   response = requests.head(link)
  #   if response.status_code == 200:
  #     print("File exists")
  #   elif response.status_code == 404:
  #     print("File not found")
  #   else:
  #     print("Received unexpected status code")
  #  except requests.Connectionerror:
  #    print("Couldn't connect to the server")


def dropdown_selection(driver,val,element_xpath):
   page_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,element_xpath)))
   page_element_dropdown = Select(page_element)
   page_element_dropdown.select_by_visible_text(val)

def fields_validation(driver,field_xpath,field_text):
    
   webpage_field = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,field_xpath)))
   assert f"{field_text}" in webpage_field.text,f"{field_text} field validated"
   logging.info(f"{field_text} is displayed")

def verify_STAC_dashboard(metrics_page_link):

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
   dot_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="plot-d6a7b5"]//*[@aria-label="dot"][1]//*[@cx="475"][1]')))
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
   box_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="plot-d6a7b5"]//*[@aria-label="bar" and @fill="rgb(0,255,0)"]')))
   assert box_element.is_displayed(), "Box format is not displayed"
   logging.info("Box plot type is displayed")

   driver.quit()

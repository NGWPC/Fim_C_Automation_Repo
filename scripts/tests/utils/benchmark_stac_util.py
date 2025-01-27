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

metrics_page_title = (By.XPATH,'//h1[@id="cross-site-contingency-metrics"]')
stac_api_browser_page_title = (By.XPATH,'//h1')
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


def  verify_gfm_data():
   print('I am here')
   
   chrome_options = webdriver.ChromeOptions()
   chrome_options.binary_location = "/usr/bin/chromium-browser"
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument("--disable-dev-shm-usage")
   print('I am here too')
   
   service=Service("/usr/bin/chromedriver")
   driver =  webdriver.Chrome(service = service ,options=chrome_options)
   print('I am here three')
   driver.get('http://localhost:8080')
   page_url = driver.current_url
   print(page_url)
   print(driver.title)
   while True:
      page_state = driver.execute_script("return document.readyState;")
      if page_state == "complete":
          break
   print(driver.page_source)
   wait = WebDriverWait(driver,20)
   try:
     element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/collections/gfm-expanded-collection']")))
     print("Element found")
     element.click()
     updated_link = driver.current_url
     print(updated_link)
   except TimeoutException:
     print("Not found")
   #page_title = driver.find_element(By.XPATH,'//h1//span[text()="stac-fastapi"]')
   #assert "stac-fastapi" in page_title.text,"Page title is not found"
   #item = driver.find_element(By.XPATH,'//a[@href="/collections/gfm-expanded-collection"]')
   #assert "Expanded Global Flood Monitoring Collection" in item.text,"Item not found"


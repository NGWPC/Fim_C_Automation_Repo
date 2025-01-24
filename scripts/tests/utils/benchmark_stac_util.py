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


def verify_gfm_data():
   print('I am here')
   
   chrome_options = webdriver.ChromeOptions()
   chrome_options.binary_location = "/usr/bin/chromium-browser"
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument("--disable-dev-shm-usage")
   print('I am here too')
   
   service=Service(ChromeDriverManager().install())
   driver =  webdriver.Chrome(service = service ,options=chrome_options)
   driver.get('localhost:8080')
   page_url = driver.current_url
   print(page_url)
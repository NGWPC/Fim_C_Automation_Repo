import pytest
import os
from ..helpers import validate_directories_files,file_exists_and_not_empty
from ..utils import csv_util, gpkg_util

def test_fim_c_008_subcase1(test_name,load_scenario_data,scenarios,read_csv,fetch_data_file_details):
    tn = test_name + '.json'
    folder_name = 'PI1/data'
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files(directory_locations,directory_contents,flag)
    csv_file,output_csv_file = read_csv(folder_name,tn,scenarios)
    csv_util.test_extract_csv_data(csv_file,os.path.expanduser(output_csv_file))
    dir_path,output_file,expected_data_file,data_file_location = fetch_data_file_details(folder_name,tn,scenarios)
    file_path = dir_path+output_file
    file_exists_and_not_empty(file_path,"gpkg")
    # gpkg_util.validate_geo_data(dir_path,output_file,os.path.expanduser(expected_data_file),os.path.expanduser(data_file_location))
 

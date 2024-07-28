import pytest
from ..helpers import validate_directories_files
from ..helpers import run_commands
from ..utils import csv_util

def test_fim_c_008_subcase1(test_name,load_scenario_data,scenarios,read_csv,fetch_data_file_details):
    tn = test_name + '.json'
    folder_name = 'PI1'
    directory_locations,directory_contents = load_scenario_data(folder_name,tn)
    validate_directories_files(directory_locations,directory_contents)
    csv_file,output_csv_file = read_csv(folder_name,tn,scenarios)
    csv_util.test_extract_csv_data(csv_file,output_csv_file)
    dir_path,output_file,expected_data_file = fetch_data_file_details(folder_name,tn,scenarios)
    run_commands(dir_path,output_file,expected_data_file)
 

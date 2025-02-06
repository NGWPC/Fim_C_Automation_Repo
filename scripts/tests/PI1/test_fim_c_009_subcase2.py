import pytest
import os
from ..helpers import validate_directories_files

def test_fim_c_009_subcase2(test_name,load_scenario_data,scenarios,fetch_data_file_details):
    tn = test_name + '.json'
    folder_name = 'PI1/data'
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files(directory_locations,directory_contents,flag)
    # dir_path,output_file,expected_data_file,data_file_location = fetch_data_file_details(folder_name,tn,scenarios)

    # # if isinstance(output_file,list) and isinstance(data_file_location,list):
    # for out_file , data_file_loc in zip([os.path.expanduser(each_output_file) for each_output_file in output_file],[os.path.expanduser(each_data_file_location) for each_data_file_location in data_file_location ]):
    #          validate_geo_data(dir_path,out_file,os.path.expanduser(expected_data_file),data_file_loc)

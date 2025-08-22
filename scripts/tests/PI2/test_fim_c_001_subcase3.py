import pytest
import os
from ..helpers import validate_directories_files,generate_dfo_data,file_exists_and_not_empty
from ..utils import txt_util,gpkg_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_001_subcase3(test_name,load_scenario_data,scenarios,fetch_data_file_details):
    tn = test_name + '.json'
    folder_name = 'PI2/data'
    generate_dfo_data()
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    directory_locations[0] = os.path.expanduser(directory_locations[0])
    validate_directories_files(directory_locations,directory_contents,flag)
    dir_path,output_file,expected_data_file,data_file_location = fetch_data_file_details(folder_name,tn,scenarios)
    file_path = dir_path+output_file
    file_exists_and_not_empty(file_path,"gpkg")
    # gpkg_util.validate_geo_data(dir_path,output_file,os.path.expanduser(expected_data_file),os.path.expanduser(data_file_location))

import pytest
import os
from ...helpers import validate_directories_files,validate_response,validate_downloaded_content
from ...utils import csv_util,gpkg_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_TP_A_4_FIMC_HAND_subcase1(test_name,load_scenario_data,scenarios,fetch_docker_details,run_docker_script,read_csv,fetch_data_file_details,remove_file):
    tn = test_name + '.json'
    folder_name = 'PI7/data'
    docker_command,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
    run_docker_script(folder_name,tn,scenarios,docker_command)
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    # validate_directories_files(directory_locations,directory_contents,flag)
    # csv_file,output_csv_file = read_csv(folder_name,tn,scenarios)
    # csv_util.test_extract_csv_data(csv_file,output_csv_file)
    # dir_path,output_file,expected_data_file,data_file_location = fetch_data_file_details(folder_name,tn,scenarios)
    # gpkg_util.validate_geo_data(dir_path,output_file,expected_data_file,data_file_location)
    # for dir_path in dir_paths:
    #     remove_file(folder_name,tn,dir_path,scenarios)
    #     print("File removed")
    #     print(dir_path)
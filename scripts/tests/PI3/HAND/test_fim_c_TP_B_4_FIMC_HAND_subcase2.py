import pytest
import os
from ...helpers import validate_directories_files,validate_response,validate_downloaded_content
from ...utils import csv_util,gpkg_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_TP_B_4_FIMC_HAND_subcase2(test_name,load_scenario_data,scenarios,fetch_docker_details,run_docker_script,fetch_data_file_details,run_shell_script_from_directory,remove_file):
    tn = test_name + '.json'
    folder_name = 'PI7/data'
    docker_command,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
    run_docker_script(folder_name,tn,scenarios,docker_command)
    run_shell_script_from_directory(folder_name,tn,scenarios)
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files(directory_locations,directory_contents,flag)
    remove_file(folder_name,tn,dir_paths,scenarios)
    print("File removed")
    print(dir_paths)
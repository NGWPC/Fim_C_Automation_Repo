import pytest
import os
from ...helpers import validate_directories_files,verify_environment_variables

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_HAND_TP_C_subcase1(test_name,load_scenario_data,scenarios,env_file_check):
    tn = test_name + '.json'
    folder_name = 'PI3/data'
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios) #,flag
    validate_directories_files(directory_locations,directory_contents,flag) #,flag

    env_files = env_file_check(folder_name,tn,scenarios)
    for env_file_info in env_files:
        file_path = env_file_info["file_name"]
        expected_content = env_file_info["expected_content"]
        verify_environment_variables(file_path,expected_content)

import pytest
import os
from ...helpers import validate_directories_files,validate_response,validate_downloaded_content
from ...utils import tif_util,json_util,directory_util,tif_util,directory_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_TP_A_EVAL_subcase3(test_name,load_scenario_data,scenarios,run_curl_command,read_tif,fetch_directory_details,remove_file):
    tn = test_name + '.json'
    folder_name = 'PI7/data'
    docker_command,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
    run_docker_script(folder_name,tn,scenarios,docker_command)
import pytest
import os
from ..helpers import validate_directories_files,validate_response
from ..utils import tif_util,json_util,directory_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_GFM_subcase1(test_name,load_scenario_data,scenarios,run_curl_command):
    tn = test_name + '.json'
    folder_name = 'PI4/data'
    # docker_command,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
    # run_docker_script(folder_name,tn,scenarios,docker_command)
    url,headers,data, destination_response_location = run_curl_command(folder_name,tn,scenarios)
    validate_response(url,headers,data,os.path.expanduser(destination_response_location))

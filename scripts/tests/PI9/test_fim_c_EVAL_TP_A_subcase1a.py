import pytest
import os
from ..helpers import validate_directories_files,validate_response,validate_downloaded_content
from ..utils import tif_util,json_util,directory_util,tif_util,directory_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_EVAL_TP_A_subcase1a(test_name,load_scenario_data,scenarios,run_curl_command,read_tif,fetch_directory_details,remove_file):
    tn = test_name + '.json'
    folder_name = 'PI9/data'
    directory = fetch_directory_details(folder_name,tn,scenarios)
    directory_util.create_directory(os.path.expanduser(directory))
    url,headers,data, destination_response_location,content_link, output_file_location = run_curl_command(folder_name,tn,scenarios)
    validate_response(url,headers,data,os.path.expanduser(destination_response_location))
   
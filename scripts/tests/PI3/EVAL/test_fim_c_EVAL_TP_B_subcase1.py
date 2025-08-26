import pytest
import os
from ...helpers import validate_directories_files,validate_post_response
from ...utils import tif_util,json_util,directory_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_EVAL_TP_B_subcase1(test_name,load_scenario_data,scenarios,run_curl_command):
    tn = test_name + '.json'
    folder_name = 'PI3/data'
    url,headers,data, destination_response_location,content_link,downloaded_content_location = run_curl_command(folder_name,tn,scenarios)
    validate_post_response(url,headers,data,os.path.expanduser(destination_response_location))

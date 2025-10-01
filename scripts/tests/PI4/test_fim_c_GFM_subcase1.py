import pytest
import os
from ..helpers import validate_directories_files,validate_response,validate_downloaded_content
from ..utils import tif_util,json_util,directory_util,tif_util,directory_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_GFM_subcase1(test_name,load_scenario_data,scenarios,run_curl_command,read_tif,fetch_directory_details,remove_file):
    tn = test_name + '.json'
    folder_name = 'PI4/data'
    directory = fetch_directory_details(folder_name,tn,scenarios)
    directory_util.create_directory(os.path.expanduser(directory))
    url,headers,data, destination_response_location,content_link, output_file_location = run_curl_command(folder_name,tn,scenarios)
    validate_response(url,headers,data,os.path.expanduser(destination_response_location))
    validate_downloaded_content(content_link,os.path.expanduser(output_file_location))
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files([os.path.expanduser(each_directory_locations) for each_directory_locations in directory_locations ],directory_contents,flag)
    tif_source_file,tif_destination_file = read_tif(folder_name,tn,scenarios)
    tif_util.test_tif_data(os.path.expanduser(tif_source_file),os.path.expanduser(tif_destination_file))
    # remove_file(folder_name,tn,os.path.expanduser(tif_source_file),scenarios)
    remove_file(folder_name,tn,os.path.expanduser(directory),scenarios)
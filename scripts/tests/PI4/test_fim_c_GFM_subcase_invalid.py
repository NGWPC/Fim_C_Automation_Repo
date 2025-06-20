import pytest
import os
from ..helpers import validate_directories_files,validate_response,validate_downloaded_content
from ..utils import tif_util,json_util,directory_util

@pytest.mark.skip(reason="This is no longer a valid scenario")
def test_fim_c_GFM_subcase(test_name,load_scenario_data,scenarios,run_curl_command,fetch_docker_details,run_docker_script):
    tn = test_name + '.json'
    folder_name = 'PI4/data'
    docker_command,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
    run_docker_script(folder_name,tn,scenarios,docker_command)
    # url,headers,data, destination_response_location,content_link, output_file_location = run_curl_command(folder_name,tn,scenarios)
    # validate_response(url,headers,data,os.path.expanduser(destination_response_location))
    # validate_downloaded_content(content_link,os.path.expanduser(output_file_location))
    # directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    # validate_directories_files([os.path.expanduser(each_directory_locations) for each_directory_locations in directory_locations ],directory_contents,flag)

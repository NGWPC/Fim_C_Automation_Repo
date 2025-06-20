import pytest
import os
from ..helpers import validate_directories_files,validate_response,validate_downloaded_content
from ..utils import tif_util,json_util,directory_util,tif_util,directory_util,gpkg_util,copy_files_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_GFM_subcase2(test_name,load_scenario_data,scenarios,run_curl_command,read_tif,fetch_directory_details,fetch_data_file_details,fetch_source_destination_details,remove_file):
    counter = 0
    tn = test_name + '.json'
    folder_name = 'PI4/data'
    directory = fetch_directory_details(folder_name,tn,scenarios)
    directory_util.create_directory(os.path.expanduser(directory))
    url,headers,data, destination_response_location,content_link, output_file_location = run_curl_command(folder_name,tn,scenarios)
    for single_url , response_location in zip(url,[os.path.expanduser(each_response_file_location) for each_response_file_location in destination_response_location ]):
        validate_response(single_url,headers,data,response_location)
    for c_link,out_file in zip(content_link,[os.path.expanduser(each_out_file) for each_out_file in output_file_location]):
        validate_downloaded_content(c_link,out_file)
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files([os.path.expanduser(each_directory_locations) for each_directory_locations in directory_locations ],directory_contents,flag)

    tif_source_file,tif_destination_file = read_tif(folder_name,tn,scenarios)
    for tsf,tdf in zip([os.path.expanduser(each_tif_source_file) for each_tif_source_file in tif_source_file],tif_destination_file):
      tif_util.test_tif_data(tsf,tdf)
      counter= counter+1
      print(counter)
   
    remove_file(folder_name,tn,os.path.expanduser(directory),scenarios)
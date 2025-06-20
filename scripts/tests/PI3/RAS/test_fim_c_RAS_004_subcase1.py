import pytest
import os
from ...helpers import validate_directories_files
from ...utils import csv_util,vrt_util

@pytest.mark.skip(reason="This is no longer a valid scenario")
def test_fim_c_RAS_004_subcase1(test_name,load_scenario_data,scenarios,fetch_docker_details,run_docker_script,read_csv,read_vrt,remove_file):
    tn = test_name + '.json'
    folder_name = 'PI3/data'
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files(directory_locations,directory_contents,flag)
    docker_commands,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
     
    for docker_command in docker_commands:
         run_docker_script(folder_name,tn,scenarios,docker_command)
         print("The command ran successfully.")
    csv_file,output_csv_file = read_csv(folder_name,tn,scenarios)
    csv_util.test_extract_csv_data(csv_file,os.path.expanduser(output_csv_file))
    source_vrt_file,destination_vrt_file,dir_paths = read_vrt(folder_name,tn,scenarios)
    vrt_util.test_vrt_data(source_vrt_file,os.path.expanduser(destination_vrt_file))
    for dir_path in dir_paths:
        remove_file(folder_name,tn,dir_path,scenarios)
        print("File removed")
        print(dir_path)

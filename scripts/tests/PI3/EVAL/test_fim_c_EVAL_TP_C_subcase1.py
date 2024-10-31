import pytest
import os
from ...helpers import validate_directories_files
from ...utils import tif_util,json_util,directory_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_EVAL_TP_C_subcase1(test_name,load_scenario_data,scenarios,fetch_docker_details,run_docker_script,read_tif,fetch_directory_details,json_read,remove_file):
    tn = test_name + '.json'
    folder_name = 'PI3/data'
    directory = fetch_directory_details(folder_name,tn,scenarios)
    directory_util.create_directory(os.path.expanduser(directory))
    docker_commands,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
    for docker_command in docker_commands:
         run_docker_script(folder_name,tn,scenarios,docker_command)
         print("The command ran successfully.")
    directory_locations,directory_contents = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files([os.path.expanduser(each_directory_locations) for each_directory_locations in directory_locations ],directory_contents)

#     tif_source_file,tif_destination_file = read_tif(folder_name,tn,scenarios)
#     for source_file , destination_file in zip([os.path.expanduser(each_tif_source_file) for each_tif_source_file in tif_source_file],[os.path.expanduser(each_tif_destination_file) for each_tif_destination_file in tif_destination_file ]):
#           tif_util.test_tif_data(source_file,destination_file)
#     source_json_file_location,destination_json_file_location = json_read(folder_name,tn,scenarios)
#     for source_json_file , destination_json_file in zip([os.path.expanduser(each_json_source_file) for each_json_source_file in source_json_file_location],[os.path.expanduser(each_json_destination_file) for each_json_destination_file in destination_json_file_location ]):
#           json_util.validate_json( os.path.expanduser(source_json_file),os.path.expanduser(destination_json_file))
    remove_file(folder_name,tn,os.path.expanduser(directory),scenarios)
